import pyautogui
# pip install pyautogui
import time
import tkinter as tk
from tkinter import simpledialog


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


def obtener_datos():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter

    nombre_contacto = simpledialog.askstring("Contacto", "Por favor, nombre del contacto:")
    mensaje = simpledialog.askstring("Mensaje", "Por favor, ingresa el mensaje que deseas enviar:")
    num_veces = simpledialog.askinteger("Cantidad", "Por favor, ingresa cuántas veces deseas enviar el mensaje:")

    return nombre_contacto, mensaje, num_veces


def main():
    nombre, mensaje, veces = obtener_datos()
    WhatsAppAutomation.esperar_abrir_whatsapp()
    WhatsAppAutomation.seleccionar_contacto(nombre)
    WhatsAppAutomation.enviar_mensaje(mensaje, veces)

    while True:
        send_again = simpledialog.askstring("Repetir", "¿Deseas enviar otro mensaje? (Si/No):").lower()

        if send_again not in ['si', 's', 'y', 'yes']:
            print("Proceso finalizado. ¡Hasta luego!")
            break
        else:
            print("Reiniciando para enviar un nuevo mensaje...")
            nombre, mensaje, veces = obtener_datos()
            WhatsAppAutomation.esperar_abrir_whatsapp()
            WhatsAppAutomation.nuevo_mensaje()
            WhatsAppAutomation.seleccionar_contacto(nombre)
            WhatsAppAutomation.enviar_mensaje(mensaje, veces)


if __name__ == "__main__":
    main()
