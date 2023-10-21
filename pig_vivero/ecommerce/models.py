from django.db import models

# Create your models here.

# -------------------------------------------------------------------
# Clase "Cliente"
# -------------------------------------------------------------------
class Cliente(models.Model):
    numero_de_cliente = models.IntegerField(verbose_name="numero de cliente")
    nombre = models.CharField(verbose_name="nombre", max_length=250)
    apellido = models.CharField(verbose_name="apellido", max_length=250)

# -------------------------------------------------------------------
# Clase "Producto"
# -------------------------------------------------------------------
class Producto(models.Model):
    codigo = models.IntegerField(verbose_name="codigo del producto")
    descripcion = models.CharField(verbose_name="descripcion del producto", max_length=250)
    cantidad = models.IntegerField(verbose_name="cantidad en stock")
    precio = models.FloatField(verbose_name="precio del producto")

    # # Definimos el constructor e inicializamos los atributos de instancia
    # def __init__(self, codigo, descripcion, cantidad, precio):
    #     self.codigo = codigo           # Código 
    #     self.descripcion = descripcion # Descripción
    #     self.cantidad = cantidad       # Cantidad disponible (stock)
    #     self.precio = precio           # Precio 

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

    # def __init__(self):
    #     self.conexion = get_db_connection()
    #     self.cursor = self.conexion.cursor()

    def agregar_producto(self, codigo, descripcion, cantidad, precio):
        producto_existente = self.consultar_producto(codigo)
        if producto_existente:
            return jsonify({'message': 'Ya existe un producto con ese código.'}), 400
        nuevo_producto = Producto(codigo, descripcion, cantidad, precio)
        sql = f'INSERT INTO productos VALUES ({codigo}, "{descripcion}", {cantidad}, {precio});'
        self.cursor.execute(sql)
        self.conexion.commit()
        return jsonify({'message': 'Producto agregado correctamente.'}), 200
    
    def consultar_producto(self, codigo):
        sql = f'SELECT * FROM productos WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, descripcion, cantidad, precio = row
            return Producto(codigo, descripcion, cantidad, precio)
        return None
    
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio):
        producto = self.consultar_producto(codigo)
        if producto:
            producto.modificar(nueva_descripcion, nueva_cantidad, nuevo_precio)
            sql = f'UPDATE productos SET descripcion = "{nueva_descripcion}", cantidad = {nueva_cantidad}, precio = {nuevo_precio} WHERE codigo = {codigo};' 
            self.cursor.execute(sql)
            self.conexion.commit()
            return jsonify({'message': 'Producto modificado correctamente.'}), 200
        return jsonify({'message': 'Producto no encontrado.'}), 404
    
    def listar_productos(self):
        print("listar productos")
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()
        productos = []
        for row in rows:
            codigo, descripcion, cantidad, precio = row
            producto = {'codigo': codigo, 'descripcion': descripcion, 'cantidad': cantidad, 'precio': precio}
            print(f'{codigo}\t{descripcion}\t{cantidad}\t{precio}')
            productos.append(producto)
        return jsonify(productos), 200
    
    def eliminar_producto(self, codigo):
        sql = f'DELETE FROM productos WHERE codigo = {codigo};' 
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.conexion.commit()
            return jsonify({'message': 'Producto eliminado correctamente.'}), 200
        return jsonify({'message': 'Producto no encontrado.'}), 404
    
# -------------------------------------------------------------------
# Clase "Carrito"
# -------------------------------------------------------------------
class Carrito(models.Model):
    fecha_de_compra = models.DateField(verbose_name="fecha de compra")
    monto_total = models.FloatField(verbose_name="monto total de la compra")
    direccion_entrega = models.CharField(verbose_name="direccion de entrega", max_length=250)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos_carrito = models.ManyToManyField(Producto)

    # def __init__(self):
    #     self.conexion = get_db_connection()
    #     self.cursor = self.conexion.cursor()
    #     self.items = []
    
    def agregar(self, codigo, cantidad, inventario):
        producto = inventario.consultar_producto(codigo)
        if producto is None:
            return jsonify({'message': 'El producto no existe.'}), 404
        if producto.cantidad < cantidad:
            return jsonify({'message': 'Cantidad en stock insuficiente.'}), 400
        
        for item in self.items:
            if item.codigo == codigo:
                item.cantidad += cantidad
                sql = f'UPDATE productos SET cantidad = cantidad - {cantidad}  WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return jsonify({'message': 'Producto agregado al carrito correctamente.'}), 200

        nuevo_item = Producto(codigo, producto.descripcion, cantidad, producto.precio)
        self.items.append(nuevo_item)
        sql = f'UPDATE productos SET cantidad = cantidad - {cantidad}  WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        self.conexion.commit()
        return jsonify({'message': 'Producto agregado al carrito correctamente.'}), 200
    
    def quitar(self, codigo, cantidad, inventario):
        for item in self.items:
            if item.codigo == codigo:
                if cantidad > item.cantidad:
                    return jsonify({'message': 'Cantidad a quitar mayor a la cantidad en el carrito.'}), 400
                item.cantidad -= cantidad
                if item.cantidad == 0:
                    self.items.remove(item)
                sql = f'UPDATE productos SET cantidad = cantidad + {cantidad} WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return jsonify({'message': 'Producto quitado del carrito correctamente.'}), 200
        return jsonify({'message': 'El producto no se encuentra en el carrito.'}), 404

    def mostrar(self):
        productos_carrito = []
        for item in self.items:
            producto = {'codigo': item.codigo, 'descripcion': item.descripcion, 'cantidad': item.cantidad, 'precio': item.precio}
            productos_carrito.append(producto)
        return jsonify(productos_carrito), 200