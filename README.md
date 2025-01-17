# Sistema de Ventas - Sanbauben

Este proyecto es un sistema de ventas desarrollado en Python con una interfaz gráfica basada en Tkinter y una base de datos SQLite para el almacenamiento de información. Permite registrar productos, actualizar precios, gestionar un carrito de compras y finalizar ventas, manteniendo un historial de las transacciones realizadas.

---

## Características Principales

1. **Gestión de Productos:**

   - Registrar productos con código de barras, nombre, precio y descripción.
   - Actualizar el precio de productos existentes.

2. **Carrito de Compras:**

   - Escanear productos mediante su código de barras.
   - Agregar productos al carrito de manera manual.
   - Eliminar productos del carrito.

3. **Gestión de Ventas:**

   - Calcular el total del carrito en tiempo real.
   - Finalizar y registrar una venta, incluyendo detalles como productos, precios y fecha.

4. **Base de Datos SQLite:**

   - Almacena información sobre productos y ventas.
   - Estructura robusta con claves primarias y restricciones de unicidad.

5. **Interfaz Gráfica Intuitiva:**

   - Diseñada con Tkinter para facilitar la interacción del usuario.

---

## Requisitos Previos

1. **Python 3.6 o superior**: Asegúrate de tener Python instalado en tu sistema.

   - [Descargar Python](https://www.python.org/downloads/)

2. **Bibliotecas estándar**:

   - `sqlite3` (integrada en Python).
   - `tkinter` (también integrada en Python).

3. **DB Browser for SQLite** (opcional):

   - Una herramienta gráfica para explorar y administrar la base de datos SQLite.
   - Descárgalo desde [sqlitebrowser.org](https://sqlitebrowser.org).

---

## Instrucciones de Instalación

1. **Clonar o descargar el repositorio:**

   ```bash
   git clone <url-del-repositorio>
   cd sistema-ventas-sanbauben
   ```

2. **Ejecutar el script principal:**

   ```bash
   python main.py
   ```

   > Esto inicializará la base de datos (`sanbauben.db`) automáticamente y abrirá la interfaz gráfica del sistema.

3. **(Opcional) Abrir la base de datos con DB Browser:**

   - Si deseas inspeccionar directamente el contenido de la base de datos, abre el archivo `sanbauben.db` con DB Browser for SQLite.
   - Podrás explorar las tablas, editar registros y ejecutar consultas SQL de manera gráfica.

---

## Uso del Programa

### 1. **Registrar Producto**

- Haz clic en el botón **"Registrar Producto"**.
- Ingresa el código de barras, nombre, precio y descripción del producto.
- Haz clic en **"Registrar"** para guardar el producto en la base de datos.

### 2. **Actualizar Precio**

- Haz clic en el botón **"Actualizar Precio"**.
- Ingresa el código de barras del producto y el nuevo precio.
- Haz clic en **"Actualizar"** para modificar el precio.

### 3. **Escanear Productos**

- Haz clic en el botón **"Escanear Productos"**.
- Escanea o ingresa el código de barras de los productos para agregarlos al carrito.
- Usa los botones para eliminar productos, agregar manualmente o finalizar la venta.

### 4. **Finalizar Venta**

- En la ventana de escaneo, haz clic en **"Finalizar Venta"**.
- El sistema registrará la venta en la base de datos con un resumen de productos, el total y la fecha.

---

## Estructura del Código

- **`main.py`**:
  Contiene la lógica principal del programa, como la inicialización de la base de datos, definición de funciones y configuración de la interfaz gráfica.

- **Base de Datos SQLite**:

  - Tabla `productos`:
    - `id`: Identificador único del producto.
    - `codigo_barra`: Código de barras único del producto.
    - `nombre`: Nombre del producto.
    - `precio`: Precio del producto.
    - `descripcion`: Descripción opcional del producto.
  - Tabla `ventas`:
    - `venta_id`: Identificador único de la venta.
    - `productos`: Lista de productos vendidos en formato texto.
    - `total`: Total de la venta.
    - `fecha`: Fecha y hora de la venta.

---

## Contribuciones

1. Crea un fork del repositorio.
2. Realiza tus cambios en una nueva rama:
   ```bash
   git checkout -b nueva-funcionalidad
   ```
3. Haz un commit de tus cambios:
   ```bash
   git commit -m "Agregué nueva funcionalidad"
   ```
4. Envía los cambios:
   ```bash
   git push origin nueva-funcionalidad
   ```
5. Abre un Pull Request en el repositorio original.

---

##

---

## Contacto

Si tienes preguntas o problemas, no dudes en comunicarte con:

- **Autor:** [Vanina Coria developer]
- **Email:** [vaninamariselcoria75@gmail.com]

---

