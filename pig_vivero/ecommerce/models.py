from django.db import models

# Create your models here.

# -------------------------------------------------------------------
# Clase "Cliente"
# -------------------------------------------------------------------
class Cliente(models.Model):
    numero_de_cliente = models.IntegerField(verbose_name="numero de cliente")
    nombre = models.CharField(verbose_name="nombre", max_length=250)
    apellido = models.CharField(verbose_name="apellido", max_length=250)
    dni = models.IntegerField(verbose_name="DNI")


# -------------------------------------------------------------------
# Clase "Categoria"
# -------------------------------------------------------------------
class Categoria(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=250)
    descripcion = models.CharField(verbose_name="descripcion del producto", max_length=250)

    def __str__(self):
        return self.nombre
    

# -------------------------------------------------------------------
# Clase "Producto"
# -------------------------------------------------------------------
class Producto(models.Model):
    codigo = models.CharField(verbose_name="codigo del producto",max_length=250)
    nombre = models.CharField(verbose_name="nombre del producto",max_length=250)
    descripcion = models.CharField(verbose_name="descripcion del producto", max_length=250)
    precio = models.FloatField(verbose_name="precio del producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # imagen = models.ImageField(verbose_name="imagen del producto") # Esto hay que chequear si no se necesitan otras dependencias para que funcione

    # Este metodo es un auxiliar para crear mas facil los productos inicialmente
    def crear_productos(self):
        Producto1 = Producto("1lr", "lirio rojo", "Simbolismo: Amor y seducción", "8500", "lirio")
        Producto2 = Producto("1lb", "lirio blanco", "Simbolismo: Pureza y belleza", "8000", "lirio")
        Producto3 = Producto("1ln", "lirio naranja", "Simbolismo: Pasion", "8000", "lirio")
        Producto4 = Producto("1fr", "arboles frutales", "Consultar segun la temporada", "8000", "frutales")
        Producto5 = Producto("1ca", "cactus", "Fuentes de exito personal y laboral", "8000", "cactus")
        Producto6 = Producto("1gr", "gromineas", "Plantita espectacular para decorar", "8000", "gromineas")
        Producto7 = Producto("1fu", "fuentes", "Contamos con distintos modelos", "8000", "fuentes")
        Producto8 = Producto("1ma", "macetas", "Variedad de colores y modelos", "8000", "macetas")
        Producto9 = Producto("1he", "herramientas", "Palas, regaderas, mangueras y mas", "8000", "herramientas")
        Producto1.save()
        Producto2.save()
        Producto3.save()
        Producto4.save()
        Producto5.save()
        Producto6.save()
        Producto7.save()
        Producto8.save()
        Producto9.save()
    
    def __str__(self):
        return self.nombre
    
    # Este método permite modificar un producto.
    def modificar(self, nueva_descripcion, nueva_cantidad, nuevo_precio):
        self.descripcion = nueva_descripcion  # Modifica la descripción
        self.cantidad = nueva_cantidad        # Modifica la cantidad
        self.precio = nuevo_precio            # Modifica el precio


# -------------------------------------------------------------------
# Clase "ItemInventario"
# -------------------------------------------------------------------
class ItemInventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="cantidad de unidades del producto en inventario")


# -------------------------------------------------------------------
# Clase "Inventario"
# -------------------------------------------------------------------
class Inventario(models.Model):
    fecha_creacion = models.DateField(verbose_name="fecha de creacion del inventario")
    fecha_modificacion = models.DateField(verbose_name="fecha de la ultima modificacion")
    items_inventario = models.ManyToManyField(ItemInventario)

    
# -------------------------------------------------------------------
# Clase "ItemCarrito"
# -------------------------------------------------------------------
class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="cantidad de unidades del producto en carrito")


# -------------------------------------------------------------------
# Clase "Carrito"
# -------------------------------------------------------------------
class Carrito(models.Model):
    fecha_de_compra = models.DateField(verbose_name="fecha de compra")
    monto_total = models.FloatField(verbose_name="monto total de la compra")
    direccion_entrega = models.CharField(verbose_name="direccion de entrega", max_length=250)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    items_carrito = models.ManyToManyField(ItemCarrito)


