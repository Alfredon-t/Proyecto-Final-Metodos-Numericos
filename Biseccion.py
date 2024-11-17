import sympy as sp

def biseccion(f_evaluar, var, a, b, tol=1e-6, i=100): # a,b son los extremos del intervalo

    f = sp.lambdify(var, f_evaluar)  

    if f(a) * f(b) >= 0:
        raise ValueError("No se puede encontrar una raíz en el intervalo [a, b].")

    for i in range(i):
        c = (a + b) / 2  # Calcular el punto medio
        fc = f(c)

        if abs(fc) < tol or abs(b - a) < tol: # Criterio de convergencia
            return c

        # Decidir el nuevo intervalo
        if f(a) * fc < 0:
            b = c  # La raíz está entre a y c
        else:
            a = c  # La raíz está entre c y b

    raise ValueError("El método no convergió después de {} iteraciones.".format(i))
