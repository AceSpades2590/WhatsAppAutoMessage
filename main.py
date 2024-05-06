import pyautogui
import webbrowser
import tkinter as tk
from tkinter import simpledialog, messagebox
import time


class WhatsAppAutomation:
    @staticmethod
    def esperar_abrir_whatsapp():
        time.sleep(1)
        pyautogui.hotkey('win', 's')
        time.sleep(1)
        pyautogui.write('WhatsApp', interval=0.1)
        pyautogui.press('enter')
        time.sleep(2)

    @staticmethod
    def seleccionar_contacto(nombre_contacto):
        pyautogui.write(nombre_contacto, interval=0.1)
        time.sleep(1)
        pyautogui.press('tab')  # Presiona la tecla "Tab"
        time.sleep(1)
        pyautogui.press('enter')  # Presiona la tecla "Enter"

    @staticmethod
    def enviar_mensaje(mensaje, num_veces):
        time.sleep(2)
        for i in range(num_veces):
            pyautogui.write(mensaje, interval=0.01)
            pyautogui.press('enter')

    @staticmethod
    def nuevo_mensaje():
        pyautogui.press('esc', presses=5)


class Numero:
    def __init__(self, num):
        self.num = num


def obtener_datos_desktop():
    root = tk.Tk()
    root.withdraw()

    while True:
        nombre_contacto = simpledialog.askstring("Contacto", "Por favor, nombre del contacto:")
        if nombre_contacto:
            break
        else:
            messagebox.showwarning("Error", "Por favor, ingresa un nombre válido.")

    while True:
        mensaje = simpledialog.askstring("Mensaje", "Por favor, ingresa el mensaje que deseas enviar:")
        if mensaje.isdigit():
            messagebox.showwarning("Error", "Por favor, ingresa un mensaje válido (no solo números).")
        else:
            break

    while True:
        num_veces = simpledialog.askstring("Cantidad", "Por favor, ingresa cuántas veces deseas enviar el mensaje:")
        if num_veces.isdigit():
            break
        else:
            messagebox.showwarning("Error", "Por favor, ingresa un número válido.")

    return nombre_contacto, mensaje, int(num_veces)


def obtener_datos_web():
    root = tk.Tk()
    root.withdraw()

    while True:
        phone_number = simpledialog.askstring("Número de teléfono",
                                              "Por favor, ingresa el número de teléfono (sin el código de país):")
        if phone_number.isdigit():
            break
        else:
            messagebox.showwarning("Error", "Por favor, ingresa un número de teléfono válido (solo números).")

    while True:
        message = simpledialog.askstring("Mensaje", "Por favor, ingresa el mensaje que deseas enviar:")
        if message.isdigit():
            messagebox.showwarning("Error", "Por favor, ingresa un mensaje válido (no solo números).")
        else:
            break

    while True:
        num_times = simpledialog.askstring("Cantidad", "Por favor, ingresa cuántas veces deseas enviar el mensaje:")
        if num_times.isdigit():
            break
        else:
            messagebox.showwarning("Error", "Por favor, ingresa un número válido.")

    phone_number_with_prefix = "+" + phone_number
    return phone_number_with_prefix, message, int(num_times)




def main():
    def select_platform(platform):
        root.destroy()  # Cerrar la ventana principal antes de pasar al siguiente menú
        if platform == "desktop":
            nombre, mensaje, veces = obtener_datos_desktop()
            WhatsAppAutomation.esperar_abrir_whatsapp()
            WhatsAppAutomation.seleccionar_contacto(nombre)
            WhatsAppAutomation.enviar_mensaje(mensaje, veces)
        elif platform == "web":
            phone_number, message, num_times = obtener_datos_web()
            webbrowser.open('http://web.whatsapp.com/send?phone=' + phone_number)
            time.sleep(10)
            for i in range(num_times):
                pyautogui.typewrite(message)
                pyautogui.press('enter')
        else:
            print("Opción no válida. Por favor, seleccione 'desktop' o 'web'.")

        send_again = simpledialog.askstring("Repetir", "¿Deseas enviar otro mensaje? (Si/No):").lower()
        if send_again in ['si', 's', 'y', 'yes']:
            main()  # Volver al menú principal
        else:
            messagebox.showinfo("Despedida", "¡Hasta luego!")
            root.quit()  # Cerrar el programa

    root = tk.Tk()
    root.title("Menú Principal")
    root.geometry("300x150")

    # Obtener la resolución de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana en la pantalla
    x = (screen_width - root.winfo_reqwidth()) / 2
    y = (screen_height - root.winfo_reqheight()) / 2

    root.geometry("+%d+%d" % (x, y))  # Establecer la geometría centrada en la pantalla

    label = tk.Label(root, text="¿Deseas usar WhatsApp Desktop o WhatsApp Web?")
    label.pack(pady=20)

    desktop_button = tk.Button(root, text="WhatsApp Desktop", command=lambda: select_platform("desktop"))
    desktop_button.pack(pady=5)

    web_button = tk.Button(root, text="WhatsApp Web", command=lambda: select_platform("web"))
    web_button.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
