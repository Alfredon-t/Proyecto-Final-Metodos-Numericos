import tkinter as tk
from tkinter import messagebox
from NewtonRapson import newton_raphson
from Biseccion import biseccion
from PuntoFijo import punto_fijo
import sympy as sp


def centrar(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


def abrir_nr():
    principal.withdraw()
    pantalla_nr()


def abrir_bs():
    principal.withdraw()
    pantalla_bs()


def abrir_pf():
    principal.withdraw()
    pantalla_pf()


def regresar_al_menu(ventana):
    ventana.destroy()
    principal.deiconify()


# Ventana para Newton-Raphson
def pantalla_nr():
    ventana = tk.Toplevel()
    ventana.title("Método de Newton-Raphson")
    centrar(ventana, 400, 400)

    tk.Label(ventana, text="Método de Newton-Raphson",
             font=("Arial", 16)).pack(pady=10)
    tk.Label(ventana, text="Función (en términos de x):").pack(pady=5)
    funcion_entry = tk.Entry(ventana, width=40)
    funcion_entry.pack(pady=5)

    tk.Label(ventana, text="x inicial (x0):").pack(pady=5)
    aproximacion_entry = tk.Entry(ventana, width=20)
    aproximacion_entry.pack(pady=5)

    tk.Label(ventana, text="Convergencia:").pack(pady=5)
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

    tk.Button(ventana, text="Calcular raíz",
              command=calcular_raiz).pack(pady=20)
    tk.Button(ventana, text="Regresar al menú principal",
              command=lambda: regresar_al_menu(ventana)).pack(pady=10)


# Ventana para Bisección
def pantalla_bs():
    ventana = tk.Toplevel()
    ventana.title("Método de Bisección")
    centrar(ventana, 450, 500)

    tk.Label(ventana, text="Método de Bisección",
             font=("Arial", 16)).pack(pady=10)
    tk.Label(ventana, text="Función (en términos de x):").pack(pady=5)
    funcion_entry = tk.Entry(ventana, width=40)
    funcion_entry.pack(pady=5)

    tk.Label(ventana, text="Extremo [a]:").pack(pady=5)
    a_entry = tk.Entry(ventana, width=20)
    a_entry.pack(pady=5)

    tk.Label(ventana, text="Extremo [b]:").pack(pady=5)
    b_entry = tk.Entry(ventana, width=20)
    b_entry.pack(pady=5)

    tk.Label(ventana, text="Error:").pack(pady=5)
    tolerancia_entry = tk.Entry(ventana, width=20)
    tolerancia_entry.insert(0, "1e-6")
    tolerancia_entry.pack(pady=5)

    tk.Label(ventana, text="Número máximo de iteraciones:").pack(
        pady=5)
    iteraciones_entry = tk.Entry(ventana, width=20)
    iteraciones_entry.insert(0, "100")
    iteraciones_entry.pack(pady=5)

    def calcular_raiz_biseccion():
        try:
            expr_str = funcion_entry.get()
            a = float(a_entry.get())
            b = float(b_entry.get())
            tol = float(tolerancia_entry.get())
            max_iter = int(iteraciones_entry.get())

            x = sp.Symbol('x')
            funcion = sp.sympify(expr_str)
            raiz = biseccion(funcion, x, a, b, tol, max_iter)

            messagebox.showinfo("Resultado", f"La raíz aproximada es: {raiz}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Calcular raíz",
              command=calcular_raiz_biseccion).pack(pady=20)
    tk.Button(ventana, text="Regresar al menú principal",
              command=lambda: regresar_al_menu(ventana)).pack(pady=10)

# Ventana para punto fijo


def pantalla_pf():
    ventana = tk.Toplevel()
    ventana.title("Método de Punto Fijo")
    centrar(ventana, 500, 600)

    tk.Label(ventana, text="Método de Punto Fijo",
             font=("Arial", 16)).pack(pady=10)

    # Campo para f(x)
    tk.Label(ventana, text="Función f(x):").pack(pady=5)
    funcion_f_entry = tk.Entry(ventana, width=40)
    funcion_f_entry.pack(pady=5)

    # Campo para g(x)
    tk.Label(ventana, text="Función g(x):").pack(pady=5)
    funcion_g_entry = tk.Entry(ventana, width=40)
    funcion_g_entry.pack(pady=5)

    # Campo para x0
    tk.Label(ventana, text="Valor inicial (x0):").pack(pady=5)
    x0_entry = tk.Entry(ventana, width=20)
    x0_entry.insert(0, "0.5")  # Valor inicial por defecto
    x0_entry.pack(pady=5)

    # Campo para tolerancia
    tk.Label(ventana, text="Error (tolerancia):").pack(pady=5)
    tolerancia_entry = tk.Entry(ventana, width=20)
    tolerancia_entry.insert(0, "1e-6")  # Tolerancia por defecto
    tolerancia_entry.pack(pady=5)

    # Campo para número máximo de iteraciones
    tk.Label(ventana, text="Número máximo de iteraciones:").pack(pady=5)
    iteraciones_entry = tk.Entry(ventana, width=20)
    iteraciones_entry.insert(0, "50")  # Iteraciones por defecto
    iteraciones_entry.pack(pady=5)

    def calcular():
        try:
            # Obtener entradas del usuario
            funcion_f_str = funcion_f_entry.get()  # f(x) ingresado por el usuario
            funcion_g_str = funcion_g_entry.get()  # g(x) ingresado por el usuario

            if not funcion_f_str or not funcion_g_str:
                raise ValueError("Debe ingresar ambas funciones f(x) y g(x).")

            # Convertir entradas a expresiones de Sympy
            x = sp.Symbol('x')
            funcion_f = sp.sympify(funcion_f_str)
            funcion_g = sp.sympify(funcion_g_str)

            # Leer el resto de los parámetros
            x0 = float(x0_entry.get())
            tol = float(tolerancia_entry.get())
            max_iter = int(iteraciones_entry.get())

            # Llamar al método de punto fijo
            raiz, resultados = punto_fijo(
                funcion_f, funcion_g, x0, tol, max_iter)

            # Construir el texto del resultado
            if raiz is not None:
                resultado_texto = f"Raíz aproximada: {float(raiz):.4f}\n"
                resultado_texto += f"Iteraciones: {len(resultados) - 1}\n\n"
                resultado_texto += "Detalles de las iteraciones:\n"
                for iteracion, valor, error, f_valor in resultados:
                    error_texto = f"{
                        error:.4e}" if error is not None else "N/A"
                    f_valor_texto = f"{
                        f_valor:.4e}" if f_valor is not None else "N/A"
                    resultado_texto += f"Iteración {iteracion}: x = {float(valor):.4f},\t Error = {
                        error_texto}, \t f(x) = {f_valor_texto}\n"
            else:
                resultado_texto = "El método no converge en las iteraciones dadas."

            # Mostrar resultados
            messagebox.showinfo("Resultado", resultado_texto)

        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")

    # Botón para calcular
    tk.Button(ventana, text="Calcular raíz", command=calcular).pack(pady=20)
    # Botón para regresar al menú principal
    tk.Button(ventana, text="Regresar al menú principal",
              command=lambda: regresar_al_menu(ventana)).pack(pady=10)


principal = tk.Tk()
principal.title("Proyecto Final Métodos Numéricos")
centrar(principal, 450, 220)

tk.Label(principal, text="Métodos Iterativos",
         font=("Arial", 18)).pack(pady=20)

tk.Button(principal, text="Método de Newton-Raphson",
          command=abrir_nr, width=30).pack(pady=5)
tk.Button(principal, text="Método de Bisección",
          command=abrir_bs, width=30).pack(pady=5)
tk.Button(principal, text="Método de Punto Fijo",
          command=abrir_pf, width=30).pack(pady=5)

principal.mainloop()
