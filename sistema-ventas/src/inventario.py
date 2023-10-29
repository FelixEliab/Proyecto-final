import sqlite3
import prettytable

# Función para validar si un producto existe en el inventario
def validar_producto(codigo):
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM productos WHERE codigo = ?', (codigo,))
        if cursor.fetchone() is not None:
            return True
        return False

# Función para validar si la tabla de productos existe
def validar_tabla_productos():
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM productos')
        except sqlite3.OperationalError:
            return False
        return True

# Función para listar todos los productos en el inventario
def listar_productos():
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        if not validar_tabla_productos():
            print('No hay productos registrados.\n')
            return
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        if not productos:
            print('No hay productos registrados.')
            return
        tabla = prettytable.PrettyTable()
        tabla.field_names = ['Código', 'Nombre', 'Existencia', 'Proveedor', 'Precio']
        for producto in productos:
            tabla.add_row(producto)
        print(f"{tabla}\n")

# Función para crear un nuevo producto
def crear_producto(codigo, nombre, existencia, proveedor, precio):
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        if not validar_tabla_productos():
            cursor.execute('CREATE TABLE productos (codigo text, nombre text, existencia integer, proveedor text, precio real)')
        if validar_producto(codigo):
            print(f"El producto con código {codigo} ya existe en la tabla.")
            return
        cursor.execute('INSERT INTO productos VALUES (?, ?, ?, ?, ?)', (codigo, nombre, existencia, proveedor, precio))
        conn.commit()
        print('Producto creado exitosamente.')

# Función para actualizar un producto existente
def actualizar_producto(codigo, nombre, existencia, proveedor, precio):
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        if not validar_tabla_productos():
            print('No hay productos registrados.\n')
            return
        if not validar_producto(codigo):
            print(f"El producto con código {codigo} no existe en la tabla.")
            return
        cursor.execute('UPDATE productos SET nombre=?, existencia=?, proveedor=?, precio=? WHERE codigo=?', (nombre, existencia, proveedor, precio, codigo))
        conn.commit()
        print('Producto actualizado exitosamente.')

# Función para editar la cantidad de existencias de un producto existente
def editar_existencias(codigo, cantidad):
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        if not validar_tabla_productos():
            print('No hay productos registrados.\n')
            return
        if not validar_producto(codigo):
            print(f"El producto con código {codigo} no existe en la tabla.")
            return
        cursor.execute('UPDATE productos SET existencia=? WHERE codigo=?', (cantidad, codigo))
        conn.commit()
        print('Existencias actualizadas exitosamente.')

# Función para eliminar un producto existente
def eliminar_producto(codigo):
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        if not validar_tabla_productos():
            print('No hay productos registrados.\n')
            return
        if not validar_producto(codigo):
            print(f"El producto con código {codigo} no existe en la tabla.")
            return
        cursor.execute('DELETE FROM productos WHERE codigo=?', (codigo,))
        conn.commit()
        print('Producto eliminado exitosamente.')