# **Documentación del Sistema de Ventas - Sanbauben**

## **Descripción General**

El sistema de ventas Sanbauben es una aplicación de escritorio desarrollada en Python utilizando la biblioteca Tkinter para la interfaz gráfica y SQLite como base de datos. Este sistema permite gestionar el inventario de productos, registrar ventas y realizar cálculos de totales diarios.

---

## **Estructura de la Base de Datos**

El sistema utiliza una base de datos SQLite llamada `sanbauben.db`. Esta base de datos contiene las siguientes tablas:

### **Tabla: productos**

| **Campo**      | **Tipo** | **Descripción**                    |
| -------------- | -------- | ---------------------------------- |
| `id`           | INTEGER  | Identificador único del producto.  |
| `codigo_barra` | TEXT     | Código único del producto.         |
| `nombre`       | TEXT     | Nombre del producto.               |
| `precio`       | REAL     | Precio del producto.               |
| `descripcion`  | TEXT     | Descripción opcional del producto. |

- **Funcionalidad**: Esta tabla almacena los datos básicos de los productos registrados en el sistema.

### **Tabla: ventas**

| **Campo**   | **Tipo** | **Descripción**                     |
| ----------- | -------- | ----------------------------------- |
| `venta_id`  | INTEGER  | Identificador único de la venta.    |
| `productos` | TEXT     | Detalles de los productos vendidos. |
| `total`     | REAL     | Monto total de la venta.            |
| `fecha`     | TEXT     | Fecha y hora de la venta.           |

- **Funcionalidad**: Registra cada venta realizada, incluyendo los productos vendidos, el total y la fecha.

### **Tabla: ventas\_diarias**

| **Campo** | **Tipo** | **Descripción**                   |
| --------- | -------- | --------------------------------- |
| `id`      | INTEGER  | Identificador único del registro. |
| `fecha`   | TEXT     | Fecha del registro diario.        |
| `total`   | REAL     | Total de las ventas del día.      |

- **Funcionalidad**: Almacena los totales diarios calculados, permitiendo consultar el rendimiento de las ventas por día.

---

## **Funcionalidades del Sistema**

### **1. Registrar Productos**

- **Descripción**: Permite agregar nuevos productos al inventario.
- **Uso**: Desde la interfaz, se ingresan el código de barras, nombre, precio y descripción del producto.
- **Base de Datos**: Los datos se guardan en la tabla `productos`.

### **2. Escanear Productos y Registrar Ventas**

- **Descripción**: Facilita el registro de ventas mediante el escaneo o ingreso manual de códigos de barras.
- **Uso**:
  1. Escanea o ingresa el código de barras del producto.
  2. Agrega los productos al carrito.
  3. Finaliza la venta para registrar el total en la tabla `ventas`.

### **3. Agregar Productos Manualmente**

- **Descripción**: Permite registrar productos directamente en el carrito sin necesidad de un código de barras.
- **Uso**:
  1. En la ventana de escaneo, haz clic en "Agregar Manualmente".
  2. Ingresa el nombre del producto y su precio.
  3. El producto se añadirá al carrito y se incluirá en la venta al finalizar.

### **4. Actualizar Precios**

- **Descripción**: Modifica el precio de productos existentes.
- **Uso**: Se ingresa el código de barras y el nuevo precio en la interfaz.
- **Base de Datos**: Se actualiza el campo `precio` en la tabla `productos`.

### **5. Calcular Total del Día**

- **Descripción**: Calcula y registra automáticamente el total de las ventas realizadas en el día.
- **Uso**: Al presionar el botón "Calcular Total del Día", se muestra el total y se almacena en la tabla `ventas_diarias`.

---

## **Guía de Instalación**

### **Requisitos Previos**

1. **Instalar Python**:

   - Descarga e instala Python 3.6 o superior desde [python.org](https://www.python.org/).
   - Asegúrate de incluir Python en el PATH durante la instalación.

2. **Instalar DB Browser for SQLite** (opcional):

   - Descarga e instala [DB Browser for SQLite](https://sqlitebrowser.org/) para visualizar y gestionar la base de datos fácilmente.

### **Instalación del Sistema**

1. **Descargar el Proyecto**:

   - Copia el archivo `sanbauben.py` en la computadora del cliente.

2. **Ejecutar el Sistema**:

   - Abre una terminal o consola.
   - Navega a la ubicación del archivo `sanbauben.py`.
   - Ejecuta el programa con:
     ```bash
     python sanbauben.py
     ```

3. **Generación Automática de la Base de Datos**:

   - La primera vez que se ejecute el programa, se generará automáticamente el archivo `sanbauben.db` con las tablas necesarias.

---

## **Guía de Uso**

1. **Registrar un Producto**:

   - Haz clic en "Registrar Producto".
   - Completa los campos del formulario.
   - Presiona "Registrar" para guardar el producto.

2. **Registrar una Venta**:

   - Haz clic en "Escanear Productos".
   - Escanea o ingresa manualmente los códigos de los productos.
   - Finaliza la venta para registrar los datos.

3. **Agregar un Producto Manualmente**:

   - En la ventana de escaneo, haz clic en "Agregar Manualmente".
   - Ingresa el nombre del producto y el precio.
   - El producto se añadirá al carrito.

4. **Actualizar Precio**:

   - Haz clic en "Actualizar Precio".
   - Ingresa el código de barras y el nuevo precio.
   - Presiona "Actualizar".

5. **Calcular Total del Día**:

   - Haz clic en "Calcular Total del Día".
   - El total del día será mostrado y registrado automáticamente.

---

## **Contacto**

- **Cliente**: Guillermo GELI
- **Desarrolladora**: Vanina Marisel Coria
- **Email**: [vaninamariselcoria75@gmail.com](mailto\:vaninamariselcoria75@gmail.com)
- **Teléfono**: 3425238984

---

¡Gracias por confiar en nuestro sistema de ventas! Si tienes dudas o necesitas soporte, no dudes en contactarnos.

