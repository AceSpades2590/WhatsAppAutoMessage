import tkinter as tk
from tkinter import messagebox
import webbrowser
import time
import pyautogui
from data_collector import DataCollector
from whatsapp_automation import WhatsAppAutomation


class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menú Principal")
        self.root.geometry("300x175")
        self.center_window()
        self.create_widgets()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.root.winfo_reqwidth()) / 2
        y = (screen_height - self.root.winfo_reqheight()) / 2
        self.root.geometry("+%d+%d" % (x, y))

    def create_widgets(self):
        label = tk.Label(self.root, text="¿Deseas usar WhatsApp Desktop o WhatsApp Web?")
        label.pack(pady=20)

        desktop_button = tk.Button(self.root, text="WhatsApp Desktop", command=lambda: self.select_platform("desktop"))
        desktop_button.pack(pady=5)

        web_button = tk.Button(self.root, text="WhatsApp Web", command=lambda: self.select_platform("web"))
        web_button.pack(pady=5)

        exit_button = tk.Button(self.root, text="Salir", command=self.exit_app)
        exit_button.pack(pady=5)

    def select_platform(self, platform):
        self.root.destroy()
        if platform == "desktop":
            nombre, mensaje, veces = DataCollector.obtener_datos_desktop()
            WhatsAppAutomation.esperar_abrir_whatsapp()
            WhatsAppAutomation.seleccionar_contacto(nombre)
            WhatsAppAutomation.enviar_mensaje(mensaje, veces)
            WhatsAppAutomation.cerrar_whatsapp()
        elif platform == "web":
            phone_number, message, num_times = DataCollector.obtener_datos_web()
            webbrowser.open('http://web.whatsapp.com/send?phone=' + phone_number)
            time.sleep(10)
            for _ in range(num_times):
                pyautogui.typewrite(message)
                pyautogui.press('enter')
            pyautogui.hotkey('ctrl', 'w')
        else:
            print("Opción no válida. Por favor, seleccione 'desktop' o 'web'.")

        self.ask_send_again()

    def ask_send_again(self):
        response = messagebox.askquestion("Repetir", "¿Deseas enviar otro mensaje?", icon='question')
        if response == 'yes':
            self.root.quit()  # Salir del mainloop actual
            MainApp()  # Crear una nueva instancia de MainApp
        else:
            self.exit_app()

    def exit_app(self):
        messagebox.showinfo("Despedida", "¡Hasta luego!")
        self.root.quit()  # Salir del mainloop actual
