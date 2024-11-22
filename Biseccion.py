import sympy as sp


def biseccion(funcion, x, a, b, tol=1e-6, i=100):
    fa = funcion.subs(x, a)
    fb = funcion.subs(x, b)

    if fa * fb > 0:
        raise ValueError("La función no cambia de signo en el intervalo dado.")

    for i in range(i):
        c = (a + b) / 2
        fc = funcion.subs(x, c)

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    raise ValueError("El método no converge.")
