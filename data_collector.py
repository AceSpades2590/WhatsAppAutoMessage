import tkinter as tk
from tkinter import simpledialog, messagebox


class DataCollector:
    @staticmethod
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
            num_veces = simpledialog.askstring("Cantidad", "Por favor, ingresa cuántas veces deseas enviar "
                                                           "el mensaje:")
            if num_veces.isdigit():
                break
            else:
                messagebox.showwarning("Error", "Por favor, ingresa un número válido.")

        return nombre_contacto, mensaje, int(num_veces)

    @staticmethod
    def obtener_datos_web():
        root = tk.Tk()
        root.withdraw()

        while True:
            phone_number = simpledialog.askstring("Número de teléfono", "Por favor, ingresa el número de "
                                                                        "teléfono sin espacios (incluye el código de "
                                                                        "país, sin el +):")
            if phone_number.isdigit():
                break
            else:
                messagebox.showwarning("Error", "Por favor, ingresa un número de teléfono válido (solo "
                                                "números).")

        while True:
            message = simpledialog.askstring("Mensaje", "Por favor, ingresa el mensaje que deseas enviar:")
            if message.isdigit():
                messagebox.showwarning("Error", "Por favor, ingresa un mensaje válido (no solo números).")
            else:
                break

        while True:
            num_times = simpledialog.askstring("Cantidad", "Por favor, ingresa cuántas veces deseas enviar "
                                                           "el mensaje:")
            if num_times.isdigit():
                break
            else:
                messagebox.showwarning("Error", "Por favor, ingresa un número válido.")

        phone_number_with_prefix = "+" + phone_number
        return phone_number_with_prefix, message, int(num_times)
