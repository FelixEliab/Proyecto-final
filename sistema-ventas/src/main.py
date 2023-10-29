import sys
import sqlite3
from inventario import *
from clientes import *
from ventas import *
from reportes import *

conn = sqlite3.connect('db/ventas.db')
conn.close()

tabla = prettytable.PrettyTable()
tabla.field_names = ["Nombre", "Carnet"]
tabla.add_row(["Luis Enrique Portillo Orellana", "0907-22-15191"])
tabla.add_row(["Felix Eliab Hernandez Alarcon", "0907-22-9244"])
tabla.add_row(["Ileana Merary Pimentel Marroquín", "0907-22-9821"])

# Menú principal
def menu_principal():
    while True:
        print("Bienvenido al sistema de ventas")
        print("Seleccione una opción:")
        print("1. Inventario")
        print("2. Clientes")
        print("3. Ventas")
        print("4. Reportes")
        print("5. Salir")
        print("6. Integrantes")
        opcion = input("Opción: ")

        if opcion == "1":
            menu_inventario()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "5":
            sys.exit()
        elif opcion == "6":
            print(tabla)
        else:
            print("Opción inválida")

# Menú de inventario
def menu_inventario():
    while True:
        print("Menú de inventario")
        print("Seleccione una opción:")
        print("1. Listar productos")
        print("2. Crear producto")
        print("3. Actualizar producto")
        print("4. Editar existencias")
        print("5. Eliminar producto")
        print("6. Volver al menú principal")
        opcion = input("Opción: ")

        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            existencia = input("Existencia: ")
            proveedor = input("Proveedor: ")
            precio = input("Precio: ")
            crear_producto(codigo, nombre, existencia, proveedor, precio)
        elif opcion == "3":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            existencia = input("Existencia: ")
            proveedor = input("Proveedor: ")
            precio = input("Precio: ")
            actualizar_producto(codigo, nombre, existencia, proveedor, precio)
        elif opcion == "4":
            codigo = input("Código: ")
            cantidad = input("Cantidad: ")
            editar_existencias(codigo, cantidad)
        elif opcion == "5":
            codigo = input("Código: ")
            eliminar_producto(codigo)
        elif opcion == "6":
            break
        else:
            print("Opción inválida")

# Menú de clientes
def menu_clientes():
    while True:
        print("Menú de clientes")
        print("Seleccione una opción:")
        print("1. Listar clientes")
        print("2. Crear cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")
        opcion = input("Opción: ")

        if opcion == "1":
            listar_clientes()
        elif opcion == "2":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            crear_cliente(codigo, nombre, direccion)
        elif opcion == "3":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            actualizar_cliente(codigo, nombre, direccion)
        elif opcion == "4":
            codigo = input("Código: ")
            eliminar_cliente(codigo)
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

# Menú de ventas
def menu_ventas():
    while True:
        print("Menú de ventas")
        print("Seleccione una opción:")
        print("1. Crear venta")
        print("2. Listar ventas")
        print("3. Anular venta")
        print("4. Volver al menú principal")
        opcion = input("Opción: ")

        if opcion == "1":
            codigo_producto = input("Código de producto: ")
            codigo_cliente = input("Código de cliente: ")
            cantidad = input("Cantidad: ")
            crear_venta(codigo_producto, codigo_cliente, cantidad)
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            codigo_venta = input("Código de venta: ")
            anular_venta(codigo_venta)
        elif opcion == "4":
            break
        else:
            print("Opción inválida")

# Menú de reportes
def menu_reportes():
    while True:
        print("Menú de reportes")
        print("Seleccione una opción:")
        print("1. Ventas por producto")
        print("2. Ventas por cliente")
        print("3. Volver al menú principal")
        opcion = input("Opción: ")
        if opcion == "1":
            destinatario = input("Correo electrónico: ")
            ventas_por_producto(destinatario)
        elif opcion == "2":
            destinatario = input("Correo electrónico: ")
            ventas_por_cliente(destinatario)
        elif opcion == "3":
            break
        else:
            print("Opción inválida")

def menu_argumentos():

    if sys.argv[1] == 'inventario':
        if sys.argv[2] == 'listar':
            listar_productos()
        elif sys.argv[2] == 'crear':
            crear_producto(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
        elif sys.argv[2] == 'actualizar':
            actualizar_producto(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
        elif sys.argv[2] == 'editar-existencias':
            editar_existencias(sys.argv[3], sys.argv[4])
        elif sys.argv[2] == 'eliminar':
            eliminar_producto(sys.argv[3])
    elif sys.argv[1] == 'clientes':
        if sys.argv[2] == 'listar':
            listar_clientes()
        elif sys.argv[2] == 'crear':
            crear_cliente(sys.argv[3], sys.argv[4], sys.argv[5])
        elif sys.argv[2] == 'actualizar':
            actualizar_cliente(sys.argv[3], sys.argv[4], sys.argv[5])
        elif sys.argv[2] == 'eliminar':
            eliminar_cliente(sys.argv[3])
    elif sys.argv[1] == 'ventas':
        if sys.argv[2] == 'listar':
            listar_ventas()
        elif sys.argv[2] == 'crear':
            crear_venta(sys.argv[3], sys.argv[4], sys.argv[5])
        elif sys.argv[2] == 'anular':
            anular_venta(sys.argv[3])
    elif sys.argv[1] == 'reportes':
        if sys.argv[2] == 'ventas-por-producto':
            ventas_por_producto(sys.argv[3])
        elif sys.argv[2] == 'ventas-por-cliente':
            ventas_por_cliente(sys.argv[3])
    elif sys.argv[1] == 'integrantes':
        print(tabla)
    else:
        print("Opción inválida")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        menu_argumentos()
    else:
        menu_principal()