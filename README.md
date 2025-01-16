# Documentación del Sistema de Ventas - Sanbauben

## **Descripción General**

El sistema de ventas Sanbauben es una aplicación gráfica desarrollada en Python con la biblioteca `tkinter`. Permite a los usuarios gestionar un inventario de productos, registrar nuevas ventas y calcular automáticamente el total de las compras.

La base de datos `SQLite` almacena la información de los productos y las ventas, lo que asegura persistencia y facilita la consulta de datos históricos.

---

## **Requisitos del Sistema**

1. **Python 3.6 o superior**
2. Módulos integrados:
   - `sqlite3`
   - `tkinter`
3. **Opcional**:
   - Escáner de códigos de barras compatible con teclado (USB o Bluetooth).

---

## **Funcionalidades Principales**

### **1. Registro de Productos**

Permite agregar productos con la siguiente información:

- Código de barras (único).
- Nombre.
- Precio.
- Descripción (opcional).

### **2. Escaneo de Productos**

- Simula el escaneo de productos mediante la entrada de códigos de barras.
- Calcula automáticamente el total de la venta.
- Muestra un resumen de los productos en el carrito.

### **3. Finalización de Ventas**

- Registra la venta completa en la base de datos.
- Resetea el carrito para una nueva transacción.

### **4. Actualización de Precios**

- Modifica el precio de un producto existente en la base de datos.

---

## **Estructura de la Base de Datos**

### \*\*Tabla: \*\***`productos`**

| Campo          | Tipo    | Descripción                        |
| -------------- | ------- | ---------------------------------- |
| `id`           | INTEGER | Identificador único.               |
| `codigo_barra` | TEXT    | Código único del producto.         |
| `nombre`       | TEXT    | Nombre del producto.               |
| `precio`       | REAL    | Precio del producto.               |
| `descripcion`  | TEXT    | Descripción opcional del producto. |

### \*\*Tabla: \*\***`ventas`**

| Campo       | Tipo    | Descripción                      |
| ----------- | ------- | -------------------------------- |
| `venta_id`  | INTEGER | Identificador único de la venta. |
| `productos` | TEXT    | Lista de productos vendidos.     |
| `total`     | REAL    | Monto total de la venta.         |
| `fecha`     | TEXT    | Fecha y hora de la venta.        |

---

## **Guía de Uso**

### **1. Iniciar el Programa**

Ejecuta el archivo principal:

```bash
python sanbauben_gui.py
```

### **2. Opciones del Menú Principal**

#### **Registrar Producto**

1. Haz clic en "Registrar Producto".
2. Completa los campos requeridos:
   - Código de barras.
   - Nombre del producto.
   - Precio.
   - Descripción (opcional).
3. Haz clic en "Registrar".

#### **Escanear Productos**

1. Haz clic en "Escanear Productos".
2. Escanea o ingresa manualmente el código de barras.
3. Haz clic en "Agregar" para incluir el producto en el carrito.
4. Haz clic en "Finalizar Venta" para registrar la venta y limpiar el carrito.

#### **Actualizar Precio**

1. Haz clic en "Actualizar Precio".
2. Ingresa el código de barras y el nuevo precio.
3. Haz clic en "Actualizar".

---

## **Uso de un Escáner de Códigos de Barras**

1. Conecta el escáner al puerto USB o configura el dispositivo Bluetooth.
2. Asegúrate de que el escáner esté funcionando como un teclado.
3. Coloca el cursor en el campo de entrada del código de barras y escanea el producto.

---

## **Ampliaciones Futuras**

- Generación de reportes de ventas (diarios, semanales, mensuales).
- Exportación de datos a formatos CSV o PDF.
- Gestión de inventario (control de stock).
- Implementación de descuentos y promociones.

---

## **Créditos**

Desarrollado por: VANINA CORIA -Programadora  full stack

### Contacto:

- **Email:** [vaninamariselccoria75@gmail.com](mailto\:vaninamariselccoria75@gmail.com)
- **Teléfono:** 3425238984

---

¡Gracias por usar nuestro sistema de ventas! 😊

