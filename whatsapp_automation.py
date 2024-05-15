import pyautogui
import time


class WhatsAppAutomation:
    @staticmethod
    def esperar_abrir_whatsapp():
        time.sleep(1)
        pyautogui.hotkey('win', 's')
        time.sleep(1)
        pyautogui.write('WhatsApp', interval=0.1)
        pyautogui.press('enter')
        time.sleep(5)

    @staticmethod
    def seleccionar_contacto(nombre_contacto):
        pyautogui.write(nombre_contacto, interval=0.1)
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')

    @staticmethod
    def enviar_mensaje(mensaje, num_veces):
        time.sleep(2)
        for _ in range(num_veces):
            pyautogui.write(mensaje, interval=0.01)
            pyautogui.press('enter')

    @staticmethod
    def cerrar_whatsapp():
        pyautogui.hotkey('alt', 'f4')

    @staticmethod
    def nuevo_mensaje():
        pyautogui.press('esc', presses=5)
