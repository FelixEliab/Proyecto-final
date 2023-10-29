# README

Este proyecto consiste en un sistema transaccional de ventas desarrollado en Python. El sistema permite llevar un control de inventario, clientes y ventas, y generar reportes de ventas por producto y por cliente.

## Estructura del proyecto

El proyecto tiene la siguiente estructura de archivos:

`sistema-ventas/db/ventas.db`: Este archivo es la base de datos SQLite que se utilizará para almacenar los datos del sistema.

`sistema-ventas/src/inventario.py`: Este archivo contiene las funciones para manejar el inventario.

`sistema-ventas/src/clientes.py`: Este archivo contiene las funciones para manejar los clientes.

`sistema-ventas/src/ventas.py`: Este archivo contiene las funciones para manejar las ventas.

`sistema-ventas/src/reportes.py`: Este archivo contiene las funciones para generar reportes.

`sistema-ventas/src/main.py`: Este archivo contiene el menú principal del sistema.

`sistema-ventas/README.md`: Este archivo contiene la documentación del proyecto.

`sistema-ventas/requirements.txt`: Este archivo contiene las dependencias de Python necesarias para ejecutar el proyecto.

## Funcionalidades

El sistema cuenta con las siguientes funcionalidades:

### Inventario

- Listar productos: Permite ver todos los productos en el inventario.
- Crear producto: Permite crear un nuevo producto con los datos proporcionados.
- Actualizar producto: Permite actualizar los datos de un producto existente.
- Editar existencias: Permite editar la cantidad de existencias de un producto existente.
- Eliminar producto: Permite eliminar un producto existente.

### Clientes

- Listar clientes: Permite ver todos los clientes en el sistema.
- Crear cliente: Permite crear un nuevo cliente con los datos proporcionados.
- Actualizar cliente: Permite actualizar los datos de un cliente existente.
- Eliminar cliente: Permite eliminar un cliente existente.

### Ventas

- Crear venta: Permite crear una nueva venta con los datos proporcionados.
- Listar ventas: Permite ver todas las ventas en el sistema.

### Reportes

- Ventas por producto: Genera un reporte de ventas por producto.
- Ventas por cliente: Genera un reporte de ventas por cliente.

## Uso del sistema

El sistema se puede utilizar a través del menú principal en `sistema-ventas/src/main.py`. También se puede utilizar el menú de argumentos en la línea de comandos para interactuar con las diferentes funciones. Consulte la documentación del proyecto para obtener más información.

## Dependencias

El proyecto requiere las siguientes dependencias de Python:

- sqlite3

Estas dependencias se pueden instalar a través del archivo `sistema-ventas/requirements.txt`.