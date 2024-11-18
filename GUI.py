import tkinter as tk
from tkinter import messagebox
from NewtonRapson import newton_raphson
from Biseccion import biseccion


def centrar(ventana, ancho, alto):  #Funcion para centrar las ventansa
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


#Abrir y cerrar ventanas de los métodos
def abrir_nr():
    principal.withdraw()
    pantalla_nr()


def abrir_bs():
    principal.withdraw()
    #Falta agregar el método

def abrir_pf():
    principal.withdraw()
    #Falta agregar el método

def regresar_al_menu(ventana):
    ventana.destroy()
    principal.deiconify()


# Ventana para Newton-Raphson
def pantalla_nr():
    ventana = tk.Toplevel()
    ventana.title("Método de Newton-Raphson")
    centrar(ventana,400,400)

    tk.Label(ventana, text="Método de Newton-Raphson", font=("Arial", 16)).pack(pady=10)
    tk.Label(ventana, text="Función (en términos de x):").pack(pady=5)
    funcion_entry = tk.Entry(ventana, width=40)
    funcion_entry.pack(pady=5)

    tk.Label(ventana, text="x inicial (x0):").pack(pady=5)
    aproximacion_entry = tk.Entry(ventana, width=20)
    aproximacion_entry.pack(pady=5)

    tk.Label(ventana, text="Convergencia (por defecto 1e-6):").pack(pady=5)
    tolerancia_entry = tk.Entry(ventana, width=20)
    tolerancia_entry.insert(0, "1e-6")
    tolerancia_entry.pack(pady=5)

    tk.Label(ventana, text="Número de iteraciones:").pack(pady=5)
    iteraciones_entry = tk.Entry(ventana, width=20)
    iteraciones_entry.insert(0, "100")
    iteraciones_entry.pack(pady=5)

    def calcular_raiz():
        try:
            expr_str = funcion_entry.get()
            func_expr = sp.sympify(expr_str)
            x0 = float(aproximacion_entry.get())
            tol = float(tolerancia_entry.get())
            max_iter = int(iteraciones_entry.get())
            
            x = sp.Symbol('x')
            raiz = newton_raphson(func_expr, x, x0, tol, max_iter)
            messagebox.showinfo("Resultado", f"La raíz aproximada es: {raiz}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Calcular raíz", command=calcular_raiz).pack(pady=20)
    tk.Button(ventana, text="Regresar al menú principal", command=lambda: regresar_al_menu(ventana)).pack(pady=10)


# Crear ventana principal
principal = tk.Tk()
principal.title("Proyecto Final Métodos Numéricos")
centrar(principal,500,500)

tk.Label(principal, text="Métodos Iterativos", font=("Arial", 18)).pack(pady=20)


#Botones
tk.Button(principal, text="Método de Newton-Raphson", command=abrir_nr, width=30).pack(pady=5)
tk.Button(principal, text="Método de Bisección", command=abrir_bs, width=30).pack(pady=5)
tk.Button(principal, text="Método de Punto Fijo", command=abrir_pf, width=30).pack(pady=5)

principal.mainloop()