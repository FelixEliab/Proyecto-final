import sqlite3
import prettytable


def calcular_total_venta(codigo_producto, cantidad):
    # Conecta con la base de datos
    conexion = sqlite3.connect('db/ventas.db')
    cursor = conexion.cursor()

    # Obtiene el precio del producto
    cursor.execute(
        'SELECT precio FROM productos WHERE codigo = ?', (codigo_producto,))
    precio = cursor.fetchone()[0]

    # Cierra la conexión con la base de datos
    conexion.close()

    # Calcula el total de la venta
    total = float(precio) * float(cantidad)
    return total


def descontar_stock(codigo_producto, cantidad):
    # Conecta con la base de datos
    conexion = sqlite3.connect('db/ventas.db')
    cursor = conexion.cursor()

    # Obtiene el stock del producto
    cursor.execute(
        'SELECT existencia FROM productos WHERE codigo = ?', (codigo_producto,))
    stock = cursor.fetchone()[0]

    # Resta el stock de la cantidad vendida
    stock = int(stock) - int(cantidad)

    # Actualiza el stock del producto
    cursor.execute(
        'UPDATE productos SET existencia = ? WHERE codigo = ?', (stock, codigo_producto))
    conexion.commit()

    # Cierra la conexión con la base de datos
    conexion.close()

# Valida si la tabla de ventas existe en la base de datos


def validar_tabla_ventas():
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM ventas')
        except sqlite3.OperationalError:
            return False
        return True


def validar_ventas(codigo):
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM ventas WHERE codigo_venta = ?', (codigo,))
        if cursor.fetchone() is None:
            return False
        return True

# Crea una nueva venta con los datos proporcionados


def crear_venta(codigo_producto, codigo_cliente, cantidad):
    # Conecta con la base de datos
    conexion = sqlite3.connect('db/ventas.db')
    cursor = conexion.cursor()
    if not validar_tabla_ventas():
        cursor.execute(
            'CREATE TABLE ventas (codigo_venta INTEGER PRIMARY KEY AUTOINCREMENT,codigo_producto text, codigo_cliente text, cantidad integer, total_venta real)')
    # Obtiene el total de la venta
    total_venta = calcular_total_venta(codigo_producto, cantidad)
    # Inserta los datos de la venta en la tabla correspondiente
    cursor.execute('INSERT INTO ventas (codigo_producto, codigo_cliente, cantidad, total_venta) VALUES (?, ?, ?, ?)',
                   (codigo_producto, codigo_cliente, cantidad, total_venta))
    conexion.commit()
    descontar_stock(codigo_producto, cantidad)

    # Cierra la conexión con la base de datos
    conexion.close()

# Lista todas las ventas en el sistema


def listar_ventas():
    # Conecta con la base de datos
    conexion = sqlite3.connect('db/ventas.db')
    cursor = conexion.cursor()

    if not validar_tabla_ventas():
        print("La tabla de ventas no existe")
        return
    # Obtiene todas las ventas de la tabla correspondiente
    cursor.execute('SELECT * FROM ventas')
    ventas = cursor.fetchall()

    tabla = prettytable.PrettyTable()
    tabla.field_names = ["Código venta", "Código producto",
                         "Código cliente", "Cantidad", "Total venta"]
    # Imprime las ventas
    for venta in ventas:
        tabla.add_row(venta)

    print(tabla)
    # Cierra la conexión con la base de datos
    conexion.close()

# Elimina una venta con el código proporcionado


def anular_venta(codigo_venta):
    # Conecta con la base de datos
    conexion = sqlite3.connect('db/ventas.db')
    cursor = conexion.cursor()

    if not validar_tabla_ventas():
        print("La tabla de ventas no existe")
        return
    if not validar_ventas(codigo_venta):
        print("La venta no existe")
        return

    # Elimina la venta de la tabla correspondiente
    try:
        cursor.execute('DELETE FROM ventas WHERE codigo_venta = ?',
                       (codigo_venta,))
        conexion.commit()
        print("Venta eliminada exitosamente")
    except sqlite3.Error:
        print("Error al eliminar la venta")

    # Cierra la conexión con la base de datos
    conexion.close()
