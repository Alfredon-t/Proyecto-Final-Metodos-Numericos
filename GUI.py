import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ancho = 400
alto = 300
principal = tk.Tk()
principal.title("Proyecto Final Métodos Numéricos")
pantalla_ancho = principal.winfo_screenwidth()
pantalla_alto = principal.winfo_screenheight()
x = (pantalla_ancho // 2) - (ancho // 2)
y = (pantalla_alto // 2) - (alto // 2)
principal.geometry(f"{ancho}x{alto}+{x}+{y}")

tk.Label(principal, text="Métodos Iterativos", font=("Arial", 18)).pack(pady=20)

principal.mainloop()