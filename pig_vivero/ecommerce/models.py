from django.db import models

# Create your models here.

# -------------------------------------------------------------------
# Clase "Cliente"
# -------------------------------------------------------------------
class Cliente(models.Model):
    numero_de_cliente = models.IntegerField(verbose_name="Numero de cliente")
    nombre = models.CharField(verbose_name="Nombre", max_length=250)
    apellido = models.CharField(verbose_name="Apellido", max_length=250)
    dni = models.IntegerField(verbose_name="DNI")
    email = models.EmailField(verbose_name="E-Mail", max_length=250)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - dni: {self.dni}'


# -------------------------------------------------------------------
# Clase "Producto"
# -------------------------------------------------------------------
class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre",max_length=250)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=250)
    precio = models.FloatField(verbose_name="Precio")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen del producto')
    promocion = models.BooleanField(verbose_name="Promocion")

    def __str__(self):
        return f'Nombre: {self.nombre} - Precio: {self.precio} - Cantidad: {self.cantidad} - Promocion: {self.promocion}'


    # Este método permite modificar un producto.
    def modificar(self, nueva_descripcion, nueva_cantidad, nuevo_precio, promocion):
        self.descripcion = nueva_descripcion  # Modifica la descripción
        self.cantidad = nueva_cantidad        # Modifica la cantidad
        self.precio = nuevo_precio            # Modifica el precio
        self.promocion = promocion


# -------------------------------------------------------------------
# Clase "Categoria"
# -------------------------------------------------------------------
class Categoria(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=250)
    producto = models.ManyToManyField(Producto)   #Relacion de muchos a muchos con el modelo Producto
    
    def __str__(self):
        return f'Categoria: {self.nombre}'
    

# -------------------------------------------------------------------
# Clase "ItemCarrito"
# -------------------------------------------------------------------
class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="cantidad")
    subtotal = models.FloatField(verbose_name="Subtotal")

    def __str__(self):
        return f'Producto: {self.producto} - Cantidad: {self.cantidad} - Subtotal: {self.subtotal}' 
    
    #Acá tenemos que agrear los métodos para crear el item
    # def crear_item():
    #     pass
    # def eliminar_item():
    #     pass
    # def agregar_producto():
    #     "método para incrementar en 1 la cantidad del producto que tiene el item"
    #     pass
    # def restar_producto(_):
    #     "método para decrementar en 1 la cantidad del producto que tiene el item"
    #     pass
    # def calcular_subtotal():
    #     pass


# -------------------------------------------------------------------
# Clase "Carrito"
# -------------------------------------------------------------------
class Carrito(models.Model):
    fecha_de_compra = models.DateField(verbose_name="Fecha de compra")
    monto_total = models.FloatField(verbose_name="Monto total")
    direccion_entrega = models.CharField(verbose_name="Direccion de entrega", max_length=250)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    items_carrito = models.ForeignKey(ItemCarrito, on_delete=models.CASCADE)

    def __str__(self):
        return f'Fecha: {self.fecha_de_compra} - Monto: {self.monto_total} - Cliente: {self.cliente}'
    
    #Acá tenemos que agregar los mpetodos para crear el carro
    # def crear_carro():
    #     pass
    # def eliminar_carro():
    #     pass
    # def calcular_total():