import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Configurar la base de datos
def init_db():
    """Inicializa la base de datos y crea las tablas si no existen."""
    conn = sqlite3.connect("sanbauben.db")  # Archivo de la base de datos
    cursor = conn.cursor()

    # Crear tabla de productos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_barra TEXT NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            descripcion TEXT
        )
    ''')

    # Crear tabla de ventas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            venta_id INTEGER PRIMARY KEY AUTOINCREMENT,
            productos TEXT NOT NULL,
            total REAL NOT NULL,
            fecha TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Registrar un producto
def registrar_producto(codigo_barra, nombre, precio, descripcion=""):
    """Registra un producto en la base de datos."""
    conn = sqlite3.connect("sanbauben.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO productos (codigo_barra, nombre, precio, descripcion)
            VALUES (?, ?, ?, ?)
        ''', (codigo_barra, nombre, precio, descripcion))
        conn.commit()
        messagebox.showinfo("Éxito", f"Producto '{nombre}' registrado correctamente.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", f"El código de barras '{codigo_barra}' ya está registrado.")
    finally:
        conn.close()

# Actualizar precio de un producto
def actualizar_precio(codigo_barra, nuevo_precio):
    """Actualiza el precio de un producto en la base de datos."""
    conn = sqlite3.connect("sanbauben.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM productos WHERE codigo_barra = ?", (codigo_barra,))
    producto = cursor.fetchone()

    if producto:
        cursor.execute("UPDATE productos SET precio = ? WHERE codigo_barra = ?", (nuevo_precio, codigo_barra))
        conn.commit()
        messagebox.showinfo("Éxito", f"El precio del producto '{producto[0]}' se actualizó a ${nuevo_precio:.2f}.")
    else:
        messagebox.showerror("Error", f"No se encontró un producto con el código de barras '{codigo_barra}'.")

    conn.close()

# Escanear productos y calcular el total
def escanear_productos(codigo_barra, carrito, total_label):
    """Simula el escaneo de productos y actualiza el carrito y total."""
    conn = sqlite3.connect("sanbauben.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nombre, precio FROM productos WHERE codigo_barra = ?", (codigo_barra,))
    producto = cursor.fetchone()

    if producto:
        nombre, precio = producto
        carrito.append((nombre, precio))
        total = sum(item[1] for item in carrito)
        total_label.config(text=f"Total: ${total:.2f}")
        return True, carrito
    else:
        messagebox.showerror("Error", "Producto no encontrado. Intente nuevamente.")
        return False, carrito

# Finalizar venta
def finalizar_venta(carrito):
    """Guarda la venta en la base de datos y muestra el total."""
    if not carrito:
        messagebox.showerror("Error", "El carrito está vacío. No se puede finalizar la venta.")
        return

    conn = sqlite3.connect("sanbauben.db")
    cursor = conn.cursor()

    productos = ", ".join(f"{item[0]} (${item[1]:.2f})" for item in carrito)
    total = sum(item[1] for item in carrito)
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO ventas (productos, total, fecha)
        VALUES (?, ?, ?)
    ''', (productos, total, fecha_actual))

    conn.commit()
    conn.close()

    messagebox.showinfo("Venta Finalizada", f"Venta registrada con éxito. Total: ${total:.2f}")

# Interfaz gráfica principal
def main():
    init_db()

    # Ventana principal
    root = tk.Tk()
    root.title("Sistema de Ventas - Sanbauben")
    root.geometry("600x400")

    # Frame para opciones principales
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)

    def abrir_registro():
        """Abre la ventana para registrar productos."""
        registro_win = tk.Toplevel(root)
        registro_win.title("Registrar Producto")
        registro_win.geometry("400x300")

        tk.Label(registro_win, text="Código de barras:").pack(pady=5)
        codigo_entry = tk.Entry(registro_win)
        codigo_entry.pack(pady=5)

        tk.Label(registro_win, text="Nombre:").pack(pady=5)
        nombre_entry = tk.Entry(registro_win)
        nombre_entry.pack(pady=5)

        tk.Label(registro_win, text="Precio:").pack(pady=5)
        precio_entry = tk.Entry(registro_win)
        precio_entry.pack(pady=5)

        tk.Label(registro_win, text="Descripción:").pack(pady=5)
        descripcion_entry = tk.Entry(registro_win)
        descripcion_entry.pack(pady=5)

        def registrar():
            try:
                codigo = codigo_entry.get()
                nombre = nombre_entry.get()
                precio = float(precio_entry.get())
                descripcion = descripcion_entry.get()
                registrar_producto(codigo, nombre, precio, descripcion)
                registro_win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Precio inválido. Intente nuevamente.")

        tk.Button(registro_win, text="Registrar", command=registrar).pack(pady=10)

    def abrir_escaneo():
        """Abre la ventana para escanear productos."""
        escaneo_win = tk.Toplevel(root)
        escaneo_win.title("Escanear Productos")
        escaneo_win.geometry("400x300")

        carrito = []
        total_label = tk.Label(escaneo_win, text="Total: $0.00")
        total_label.pack(pady=10)

        tk.Label(escaneo_win, text="Código de barras:").pack(pady=5)
        codigo_entry = tk.Entry(escaneo_win)
        codigo_entry.pack(pady=5)

        def agregar():
            codigo = codigo_entry.get()
            if codigo:
                _, carrito_actualizado = escanear_productos(codigo, carrito, total_label)
                carrito[:] = carrito_actualizado
                codigo_entry.delete(0, tk.END)

        def finalizar():
            finalizar_venta(carrito)
            carrito.clear()
            total_label.config(text="Total: $0.00")

        tk.Button(escaneo_win, text="Agregar", command=agregar).pack(pady=10)
        tk.Button(escaneo_win, text="Finalizar Venta", command=finalizar).pack(pady=10)

    tk.Button(frame, text="Registrar Producto", command=abrir_registro).pack(fill=tk.X, pady=5)
    tk.Button(frame, text="Escanear Productos", command=abrir_escaneo).pack(fill=tk.X, pady=5)
    tk.Button(frame, text="Salir", command=root.quit).pack(fill=tk.X, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
