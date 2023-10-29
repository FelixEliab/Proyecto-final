import sqlite3
import prettytable

def validar_cliente(codigo):
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes WHERE codigo = ?', (codigo,))
        if cursor.fetchone() is None:
            return False
        return True

def validar_tabla_clientes():
    with sqlite3.connect('db/ventas.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM clientes')
        except sqlite3.OperationalError:
            return False
        return True

# Función para listar todos los clientes en la base de datos
def listar_clientes():
    # Conexión a la base de datos
    conn = sqlite3.connect('db/ventas.db')
    c = conn.cursor()
    if not validar_tabla_clientes():
        print("No hay clientes registrados.\n")
        return

    c.execute("SELECT * FROM clientes")
    clientes = c.fetchall()
    # Imprimir los resultados
    if not clientes:
        print("No hay clientes registrados.")
        return
    tabla = prettytable.PrettyTable()
    tabla.field_names = ["Código", "Nombre", "Dirección"]
    print("Lista de clientes:")
    for cliente in clientes:
        tabla.add_row(cliente)
    print(f"{tabla}\n")
    # Cerrar la conexión a la base de datos
    conn.close()

# Función para crear un nuevo cliente en la base de datos
def crear_cliente(codigo, nombre, direccion):
    # Conexión a la base de datos
    conn = sqlite3.connect('db/ventas.db')
    c = conn.cursor()
    # Datos del nuevo cliente
    datos_cliente = (codigo, nombre, direccion)
    if not validar_tabla_clientes():
        c.execute("CREATE TABLE clientes (codigo text, nombre text, direccion text)")
    if validar_cliente(codigo):
        print(f"El cliente con código {codigo} ya existe en la tabla.")
        return
    # Consulta SQL para crear un nuevo cliente
    query = "INSERT INTO clientes VALUES (?, ?, ?)"
    # Ejecutar la consulta con los datos del nuevo cliente
    c.execute(query, datos_cliente)
    # Guardar los cambios en la base de datos
    conn.commit()

    # Imprimir mensaje de confirmación
    print("Cliente creado exitosamente.")
    # Cerrar la conexión a la base de datos
    conn.close()

# Función para actualizar los datos de un cliente existente en la base de datos
def actualizar_cliente(codigo, nombre, direccion):
    # Conexión a la base de datos
    conn = sqlite3.connect('db/ventas.db')
    c = conn.cursor()

    if not validar_tabla_clientes():
        print("No hay clientes registrados.\n")
        return
    if not validar_cliente(codigo):
        print(f"El cliente con código {codigo} no existe en la tabla.")
        return
    # Consulta SQL para actualizar los datos de un cliente
    query = "UPDATE clientes SET nombre = ?, direccion = ? WHERE codigo = ?"

    # Nuevos datos del cliente
    nuevos_datos = (nombre, direccion, codigo)

    # Ejecutar la consulta con los nuevos datos del cliente
    c.execute(query, nuevos_datos)

    # Guardar los cambios en la base de datos
    conn.commit()

    # Imprimir mensaje de confirmación
    print("Cliente actualizado exitosamente.")

    # Cerrar la conexión a la base de datos
    conn.close()

# Función para eliminar un cliente existente de la base de datos
def eliminar_cliente(codigo):
    # Conexión a la base de datos
    conn = sqlite3.connect('db/ventas.db')
    c = conn.cursor()

    if not validar_tabla_clientes():
        print("No hay clientes registrados.\n")
        return
    if not validar_cliente(codigo):
        print(f"El cliente con código {codigo} no existe en la tabla.")
        return

    # Consulta SQL para eliminar un cliente
    query = "DELETE FROM clientes WHERE codigo = ?"

    # Ejecutar la consulta con el código del cliente a eliminar
    c.execute(query, (codigo,))

    # Guardar los cambios en la base de datos
    conn.commit()

    # Imprimir mensaje de confirmación
    print("Cliente eliminado exitosamente.")

    # Cerrar la conexión a la base de datos
    conn.close()