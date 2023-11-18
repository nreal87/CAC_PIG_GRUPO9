from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# -------------------------------------------------------------------
# Clase "Cliente"
# -------------------------------------------------------------------
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    numero_de_cliente = models.IntegerField(verbose_name="Numero de cliente")
    nombre = models.CharField(verbose_name="Nombre", max_length=250)
    apellido = models.CharField(verbose_name="Apellido", max_length=250)
    dni = models.IntegerField(verbose_name="DNI")
    email = models.EmailField(verbose_name="E-Mail", max_length=250)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'


# -------------------------------------------------------------------
# Clase "Categoria"
# -------------------------------------------------------------------
class Categoria(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=250)


    def __str__(self):
        return f'Categoria: {self.nombre}'
    
    def delete(self, using=None, keep_parents=False):
        #self.portada.storage.delete(self.portada.name)  # borrado fisico
        super().delete()


# -------------------------------------------------------------------
# Clase "Producto"
# -------------------------------------------------------------------
class Producto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=250)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=250)
    precio = models.FloatField(verbose_name="Precio")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen del producto')
    promocion = models.BooleanField(verbose_name="Promocion", null=True) #si lo ponemos en True se mostrara en el index
    categoria = models.ManyToManyField(Categoria)#Relacion de muchos a muchos entre Producto y Categoria

    def __str__(self):
        # return f'Nombre: {self.nombre} - Precio: {self.precio} - Cantidad: {self.cantidad} - Promocion: {self.promocion} - Cat: {self.categoria}'
        return f'{self.nombre}'


    # Este método permite modificar un producto.
    def modificar(self, nueva_descripcion, nueva_cantidad, nuevo_precio, promocion):
        self.descripcion = nueva_descripcion  # Modifica la descripción
        self.cantidad = nueva_cantidad        # Modifica la cantidad
        self.precio = nuevo_precio            # Modifica el precio
        self.promocion = promocion



# -------------------------------------------------------------------
# Clase "Carrito"
# -------------------------------------------------------------------
class Carrito(models.Model):
    monto_total = models.FloatField(verbose_name="Monto total")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    compra_abierta = models.BooleanField(verbose_name="Compra abierta",default=True)

    def __str__(self):
        return f'Cliente: {self.cliente}'
    
    #Acá tenemos que agregar los mpetodos para crear el carro
    # def crear_carro():
    #     pass
    # def eliminar_carro():
    #     pass
    # def calcular_total():


# -------------------------------------------------------------------
# Clase "ItemCarrito"
# -------------------------------------------------------------------
class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE,default=None)
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