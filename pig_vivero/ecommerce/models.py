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
    codigo = models.IntegerField(verbose_name="codigo del producto")
    nombre = models.CharField(verbose_name="nombre del producto",max_length=250)
    descripcion = models.CharField(verbose_name="descripcion del producto", max_length=250)
    cantidad = models.IntegerField(verbose_name="cantidad en stock") # este parametro aca para mi esta mal
    precio = models.FloatField(verbose_name="precio del producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(verbose_name="imagen del producto")

    def __str__(self):
        return self.nombre
    
    # Este método permite modificar un producto.
    def modificar(self, nueva_descripcion, nueva_cantidad, nuevo_precio):
        self.descripcion = nueva_descripcion  # Modifica la descripción
        self.cantidad = nueva_cantidad        # Modifica la cantidad
        self.precio = nuevo_precio            # Modifica el precio


# -------------------------------------------------------------------
# Clase "Inventario"
# -------------------------------------------------------------------
class Inventario(models.Model):
    fecha_creacion = models.DateField(verbose_name="fecha de creacion del inventario")
    fecha_modificacion = models.DateField(verbose_name="fecha de la ultima modificacion")
    productos_stock = models.ManyToManyField(Producto)
    # items_inventario = models.ManyToManyField(ItemInventario) # Esta linea reemplazaria a la anterior

    
# -------------------------------------------------------------------
# Clase "Carrito"
# -------------------------------------------------------------------
class Carrito(models.Model):
    fecha_de_compra = models.DateField(verbose_name="fecha de compra")
    monto_total = models.FloatField(verbose_name="monto total de la compra")
    direccion_entrega = models.CharField(verbose_name="direccion de entrega", max_length=250)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos_carrito = models.ManyToManyField(Producto)
    # items_carrito = models.ManyToManyField(ItemCarrito) # Esta linea reemplazaria a la anterior


# -------------------------------------------------------------------
# Clase "ItemInventario"
# -------------------------------------------------------------------
class ItemInventario(models.Model):
    producto = models.ManyToManyField(Producto)
    cantidad = models.IntegerField(verbose_name="cantidad de unidades del producto en inventario")


# -------------------------------------------------------------------
# Clase "ItemCarrito"
# -------------------------------------------------------------------
class ItemCarrito(models.Model):
    producto = models.ManyToManyField(Producto)
    cantidad = models.IntegerField(verbose_name="cantidad de unidades del producto en carrito")