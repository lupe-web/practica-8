# Importa la biblioteca CustomTkinter para crear interfaces gráficas modernas.
import customtkinter as ctk

# Importa los cuadros de mensaje.
from tkinter import messagebox


# ==========================
# CONFIGURACIÓN DE LA VENTANA
# ==========================

# Establece el modo de apariencia.
# Opciones: "dark", "light" o "system".
ctk.set_appearance_mode("dark")

# Define el color principal de los botones y controles.
# Opciones: "blue", "green", "dark-blue".
ctk.set_default_color_theme("blue")


# ===================================
# DICCIONARIO CON USUARIOS REGISTRADOS
# ===================================

# Diccionario donde:
# La clave es el nombre del usuario.
# El valor es la contraseña.
usuarios = {
    "admin": "12345",
    "profesor": "abc123",
    "estudiante": "2026"
}


# ==============================
# FUNCIÓN PARA INICIAR SESIÓN
# ==============================

def iniciar_sesion():
    # Obtiene el texto escrito en la caja Usuario.
    usuario = txt_usuario.get()

    # Obtiene el texto escrito en la caja Contraseña.
    clave = txt_clave.get()

    # Verifica si el usuario existe
    # y si la contraseña es correcta.
    if usuario in usuarios and usuarios[usuario] == clave:

        # Muestra un mensaje de bienvenida.
        messagebox.showinfo("Acceso", f"Bienvenido {usuario}")

        # Cierra la ventana de inicio de sesión.
        ventana.destroy()

        # Abre la ventana principal.
        menu_principal(usuario)

    else:
        # Si los datos son incorrectos,
        # muestra un mensaje de error.
        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )


# ======================================
# FUNCIÓN PARA ABRIR EL MENÚ PRINCIPAL
# ======================================

def menu_principal(nombre):

    # Crea una nueva ventana.
    menu = ctk.CTk()

    # Coloca el título de la ventana.
    menu.title("Sistema")

    # Define el tamaño.
    menu.geometry("600x400")

    # Evita que el usuario cambie el tamaño.
    menu.resizable(False, False)

    # Crea una etiqueta de bienvenida.
    ctk.CTkLabel(
        menu,
        text=f"Bienvenido {nombre}",
        font=("Arial", 24, "bold")
    ).pack(pady=40)

    # Botón del módulo Ventas.
    ctk.CTkButton(
        menu,
        text="Ventas",
        width=200
    ).pack(pady=10)

    # Botón Inventario.
    ctk.CTkButton(
        menu,
        text="Inventario",
        width=200
    ).pack(pady=10)

    # Botón Clientes.
    ctk.CTkButton(
        menu,
        text="Clientes",
        width=200
    ).pack(pady=10)

    # Botón para cerrar la ventana.
    ctk.CTkButton(
        menu,
        text="Salir",
        width=200,
        command=menu.destroy
    ).pack(pady=20)

    # Mantiene abierta la ventana.
    menu.mainloop()


# ===========================
# CREACIÓN DE LA VENTANA
# ===========================

# Crea la ventana principal.
ventana = ctk.CTk()

# Coloca el título de la ventana.
ventana.title("Inicio de Sesión")

# Define el tamaño.
ventana.geometry("450x450")

# Evita que el usuario cambie el tamaño.
ventana.resizable(False, False)


# ===================
# TÍTULO
# ===================

ctk.CTkLabel(
    ventana,
    text="INICIAR SESIÓN",
    font=("Arial", 28, "bold")
).pack(pady=30)


# ===================
# CAJA DE USUARIO
# ===================

# Crea la caja donde se escribe el usuario.
txt_usuario = ctk.CTkEntry(
    ventana,
    width=250,
    placeholder_text="Usuario"
)

# Coloca la caja en la ventana.
txt_usuario.pack(pady=15)


# =======================
# CAJA CONTRASEÑA
# =======================

# Crea la caja de contraseña.
txt_clave = ctk.CTkEntry(
    ventana,
    width=250,
    placeholder_text="Contraseña",
    show="*"
)

# Coloca la caja.
txt_clave.pack(pady=15)


# ======================
# BOTÓN INGRESAR
# ======================

ctk.CTkButton(
    ventana,
    text="Ingresar",
    width=250,
    command=iniciar_sesion
).pack(pady=25)


# ==========================
# INFORMACIÓN DEL EJEMPLO
# ==========================

# Muestra un usuario y contraseña de prueba.
ctk.CTkLabel(
    ventana,
    text="Usuario: admin\nContraseña: 12345",
    font=("Arial", 12)
).pack(pady=10)


# =====================
# INICIA EL PROGRAMA
# =====================

# Ejecuta la ventana y espera las acciones del usuario.
ventana.mainloop()
