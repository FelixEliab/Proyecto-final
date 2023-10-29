from email.message import EmailMessage
import mimetypes
import os
import smtplib
import sqlite3
import ssl
import openpyxl
import prettytable

def ventas_por_producto(destinatario):
    with sqlite3.connect('db/ventas.db') as conn:
        c = conn.cursor()
        c.execute('SELECT p.nombre, SUM(v.cantidad), SUM(v.total_venta) FROM ventas v JOIN productos p ON v.codigo_producto = p.codigo GROUP BY p.codigo')
        ventas = c.fetchall()
        tabla = prettytable.PrettyTable()
        tabla.field_names = ["Producto", "Cantidad vendida", "Total vendido"]
        print('Reporte de ventas por producto:')
        for venta in ventas:
            tabla.add_row(venta)
        print(tabla)

        # Crear el archivo de Excel
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Ventas por producto"
        ws.append(["Producto", "Cantidad vendida", "Total vendido"])
        for venta in ventas:
            ws.append(venta)
        wb.save("reportes/ventas_por_producto.xlsx")

        # Enviar el archivo por correo electrónico
        enviar_correo("ventas_por_producto", destinatario)

def ventas_por_cliente(destinatario):
    with sqlite3.connect('db/ventas.db') as conn:
        c = conn.cursor()
        c.execute('SELECT c.nombre, SUM(v.cantidad), SUM(v.total_venta) FROM ventas v JOIN clientes c ON v.codigo_cliente = c.codigo GROUP BY c.codigo')
        ventas = c.fetchall()
        tabla = prettytable.PrettyTable()
        tabla.field_names = ["Cliente", "Cantidad comprada", "Total gastado"]
        print('Reporte de ventas por cliente:')
        for venta in ventas:
            tabla.add_row(venta)
        print(tabla)
        # Crear el archivo de Excel
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Ventas por cliente"
        ws.append(["Cliente", "Cantidad vendida", "Total vendido"])
        for venta in ventas:
            ws.append(venta)
        wb.save("reportes/ventas_por_cliente.xlsx")

        # Enviar el archivo por correo electrónico
        enviar_correo("ventas_por_cliente", destinatario)

def enviar_correo(archivo_adjunto, destinatario):
    SERVIDOR = "in-v3.mailjet.com"
    PUERTO = 587
    DIRECCION_DE_ORIGEN = "pitapeibook@gmail.com"
    USUARIO = os.getenv("Email_user")
    CONTRASENA = os.getenv("Email_secret")
    DIRECCION_DE_DESTINO = destinatario
    ASUNTO = "Reporte de ventas"
    MENSAJE = "Reporte de ventas"
    # Crear el mensaje
    mensaje = EmailMessage()
    mensaje["From"] = DIRECCION_DE_ORIGEN
    mensaje["To"] = DIRECCION_DE_DESTINO
    mensaje["Subject"] = ASUNTO
    mensaje.set_content(MENSAJE)
    # Adjuntar el archivo
    ruta = f"reportes/{archivo_adjunto}.xlsx"
    ctype, encoding = mimetypes.guess_type(ruta)

    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"
    tipo_principal, sub_tipo = ctype.split("/", 1)
    archivo = open(ruta , "rb")
    mensaje.add_attachment(archivo.read(), maintype= tipo_principal, subtype = sub_tipo, filename = ruta)
    # Enviar el mensaje
    contexto = ssl.create_default_context()
    with smtplib.SMTP(SERVIDOR, PUERTO) as servidor:
        servidor.starttls(context=contexto)
        servidor.login(USUARIO, CONTRASENA)
        servidor.send_message(mensaje)
    print("Correo enviado")