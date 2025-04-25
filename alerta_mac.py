import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk  # Necesitarás instalar Pillow con `pip install pillow`
import getpass
import socket
import platform
import pwd

def mostrar_alerta():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal para que no se vea

    # Obtener el nombre de usuario del sistema
    nombre_usuario = getpass.getuser()
    try:
        nombre_completo = pwd.getpwuid(os.getuid()).pw_gecos.split(',')[0]
    except:
        nombre_completo = nombre_usuario

    # Obtener el apellido del nombre completo
    apellido_usuario = nombre_completo.split(' ')[-1] 
    # Obtener otros datos del sistema
    nombre_equipo = socket.gethostname()  # De socket
    direccion_ip = socket.gethostbyname(nombre_equipo)  # De socket
    sistema_operativo = platform.system()  # De platform
    version_sistema_operativo = platform.version()  # De platform
    procesador = platform.processor()  # De platform
    directorio_usuario = os.path.expanduser("~")  # De os

    # Crear la ventana de alerta
    ventana = tk.Toplevel(root)
    ventana.title("ALERTA DE SEGURIDAD")
    ventana.geometry("800x600")
    ventana.configure(bg="lightyellow")
    ventana.attributes('-topmost', True)
    ventana.grab_set()  # Hacer la ventana modal
    ventana.protocol("WM_DELETE_WINDOW", lambda: None)  # Deshabilitar botón de cerrar
    ventana.lift()  # Asegurar que la ventana esté en la parte superior

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
        f"¡SU SISTEMA HA SIDO VULNERADO,{nombre_completo.upper()}!\n\n"
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

    # Mostrar la alerta inicial
    messagebox.showwarning(
        "ALERTA DE SEGURIDAD",
        mensaje_personalizado,
        parent=ventana
    )

    # Pedir el código de cierre
    codigo_correcto = "3689"  # Cambia esto por el código que desees
    while True:
        codigo_ingresado = simpledialog.askstring("Código de Seguridad", "Ingrese el código para cerrar la alerta:", parent=ventana)
        if codigo_ingresado == codigo_correcto:
            messagebox.showinfo(
                "Acceso Concedido",
                f"Código correcto. La alerta se cerrará.\n\n"
                f"Gracias, {nombre_usuario} {apellido_usuario}, por su atención y colaboración para "
                "mantener la seguridad de nuestra empresa.",
                parent=ventana
            )
            break
        else:
            messagebox.showerror("Acceso Denegado", "Código incorrecto. Intente nuevamente.", parent=ventana)

    root.destroy()

if __name__ == "__main__":
    mostrar_alerta()