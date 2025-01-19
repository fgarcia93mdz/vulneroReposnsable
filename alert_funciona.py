import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from tkinter import simpledialog, messagebox
import getpass

def mostrar_alerta():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal para que no se vea

    # Obtener el nombre de usuario del sistema
    nombre_usuario = getpass.getuser()
    apellido_usuario = "Usuario"  # Puedes cambiar esto si puedes obtener el apellido de alguna manera

    # Mostrar ventana principal
    root.deiconify()  # Vuelve a mostrar la ventana principal
    root.title("Alerta de Seguridad")
    root.geometry("800x600")  # Ajustar tamaño si es necesario
    root.configure(bg="lightyellow")
    root.resizable(False, False)  # Bloquear redimensionar
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Deshabilitar botón de cerrar

    # Configurar la apariencia de la ventana de diálogo
    style = {
        'font': 'Helvetica 12',
        'background': 'lightyellow',
        'foreground': 'black',
        'borderwidth': 2,
        'relief': 'solid'
    }
    root.option_add('*Dialog.msg.font', style['font'])
    root.option_add('*Dialog.msg.background', style['background'])
    root.option_add('*Dialog.msg.foreground', style['foreground'])
    root.option_add('*Dialog.msg.borderWidth', style['borderwidth'])
    root.option_add('*Dialog.msg.relief', style['relief'])

    # Crear un mensaje personalizado
    mensaje_personalizado = (
        f"¡SU SISTEMA HA SIDO VULNERADO, {nombre_usuario.upper()} {apellido_usuario.upper()}!\n\n"
        "Esto es una simulación para concientizar sobre la importancia de la seguridad informática.\n"
        "Por favor, contacte al departamento de IT para obtener el código de cierre.\n\n"
        "CONSEJOS DE SEGURIDAD:\n"
        "- No comparta sus contraseñas con nadie.\n"
        "- Use contraseñas fuertes y cámbielas regularmente.\n"
        "- Mantenga su software y sistemas operativos actualizados.\n"
        "- Sea cauteloso con los correos electrónicos y enlaces sospechosos.\n"
        "- Utilice autenticación de dos factores siempre que sea posible.\n"
        "- Realice copias de seguridad de su información importante.\n"
        "- No instale software de fuentes no confiables.\n"
        "- Informe cualquier actividad sospechosa al departamento de IT inmediatamente."
    )

    # Mostrar la alerta inicial
    messagebox.showwarning(
        "ALERTA DE SEGURIDAD",
        mensaje_personalizado
    )

    # Pedir el código de cierre
    codigo_correcto = "3689"  # Cambia esto por el código que desees
    while True:
        codigo_ingresado = simpledialog.askstring("Código de Seguridad", "Ingrese el código para cerrar la alerta:", parent=root)
        if codigo_ingresado == codigo_correcto:
            messagebox.showinfo(
                "Acceso Concedido",
                f"Código correcto. La alerta se cerrará.\n\n"
                f"Gracias, {nombre_usuario} {apellido_usuario}, por su atención y colaboración para "
                "mantener la seguridad de nuestra empresa.",
                parent=root
            )
            break
        else:
            messagebox.showerror("Acceso Denegado", "Código incorrecto. Intente nuevamente.", parent=root)

    root.destroy()

if __name__ == "__main__":
    mostrar_alerta()



import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk  # Necesitarás instalar Pillow con `pip install pillow`
import getpass
import socket
import platform

def mostrar_alerta():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal para que no se vea

    # Obtener el nombre de usuario del sistema
    nombre_usuario = getpass.getuser()
    apellido_usuario = "Usuario"  # Puedes cambiar esto si puedes obtener el apellido de alguna manera

    # Obtener otros datos del sistema
    nombre_equipo = socket.gethostname()
    direccion_ip = socket.gethostbyname(nombre_equipo)
    sistema_operativo = platform.system()
    version_sistema_operativo = platform.version()
    procesador = platform.processor()
    directorio_usuario = os.path.expanduser("~")

    # Crear la ventana de alerta
    ventana = tk.Toplevel(root)
    ventana.title("ALERTA DE SEGURIDAD")
    ventana.geometry("800x600")
    ventana.configure(bg="lightyellow")
    ventana.attributes('-topmost', True)
    ventana.grab_set()  # Hacer la ventana modal
    ventana.protocol("WM_DELETE_WINDOW", lambda: None)  # Deshabilitar botón de cerrar

    # Añadir una imagen
    try:
        img = Image.open("2MLI2ZBJEVEBZCTPO5XQUFRBOM.jpg")  # Asegúrate de tener una imagen llamada "2MLI2ZBJEVEBZCTPO5XQUFRBOM.jpg" en el mismo directorio
        img = img.resize((200, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(ventana, image=img, bg="lightyellow")
        panel.pack(pady=20)
    except FileNotFoundError:
        print("Imagen no encontrada, continuando sin imagen.")

    # Crear un mensaje personalizado
    mensaje_personalizado = (
        f"¡SU SISTEMA HA SIDO VULNERADO, {nombre_usuario.upper()} {apellido_usuario.upper()}!\n\n"
        "Esto es una simulación para concientizar sobre la importancia de la seguridad informática.\n"
        "Por favor, contacte al departamento de IT para obtener el código de cierre.\n\n"
        "INFORMACIÓN DEL SISTEMA:\n"
        f"- Nombre del equipo: {nombre_equipo}\n"
        f"- Dirección IP: {direccion_ip}\n"
        f"- Sistema operativo: {sistema_operativo} {version_sistema_operativo}\n"
        f"- Procesador: {procesador}\n"
        f"- Directorio del usuario: {directorio_usuario}\n\n"
        "CONSEJOS DE SEGURIDAD:\n"
        "- No comparta sus contraseñas con nadie.\n"
        "- Use contraseñas fuertes y cámbielas regularmente.\n"
        "- Mantenga su software y sistemas operativos actualizados.\n"
        "- Sea cauteloso con los correos electrónicos y enlaces sospechosos.\n"
        "- Utilice autenticación de dos factores siempre que sea posible.\n"
        "- Realice copias de seguridad de su información importante.\n"
        "- No instale software de fuentes no confiables.\n"
        "- Informe cualquier actividad sospechosa al departamento de IT inmediatamente."
    )

    # Mostrar el mensaje en la ventana de alerta
    texto_mensaje = tk.Label(
        ventana,
        text=mensaje_personalizado,
        font=('Arial', 12),
        bg='lightyellow',
        fg='black',
        justify='left',
        wraplength=700
    )
    texto_mensaje.pack(pady=20)

    # Campo para ingresar el código de cierre
    label_codigo = tk.Label(ventana, text="Ingrese el código de seguridad:", bg='lightyellow', font=('Helvetica', 12))
    label_codigo.pack(pady=10)
    entry_codigo = tk.Entry(ventana, show='*', font=('Helvetica', 12))
    entry_codigo.pack(pady=5)

    # Botón para verificar el código
    def verificar_codigo():
        codigo_correcto = "3689"  # Cambia esto por el código que desees
        codigo_ingresado = entry_codigo.get()
        if codigo_ingresado == codigo_correcto:
            messagebox.showinfo(
                "Acceso Concedido",
                f"Código correcto. La alerta se cerrará.\n\n"
                f"Gracias, {nombre_usuario} {apellido_usuario}, por su atención y colaboración para "
                "mantener la seguridad de nuestra empresa.",
                parent=ventana
            )
            ventana.destroy()
            root.destroy()
        else:
            messagebox.showerror("Acceso Denegado", "Código incorrecto. Intente nuevamente.", parent=ventana)

    boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_codigo, bg='red', fg='white', font=('Helvetica', 12, 'bold'))
    boton_verificar.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    mostrar_alerta()    