import sympy as sp


def newton_raphson(f_evaluar, var, x0, tol=1e-6, i=100):  # i es el número de iteraciones
    f_prima = sp.diff(f_evaluar, var)
    f = sp.lambdify(var, f_evaluar)
    f_derivada = sp.lambdify(var, f_prima)

    x_n = x0
    for i in range(i):
        fx_n = f(x_n)
        f_pri_xn = f_derivada(x_n)

        if abs(f_pri_xn) < 1e-10:  # usamos 1e-10 para representar a 0
            raise ValueError("Error. La función no se puede evaluar")

        x_sig = x_n - (fx_n / f_pri_xn)  # Formula de Newton-Raphson

        if abs(x_sig - x_n) < tol:
            return x_sig

        x_n = x_sig

    raise ValueError(
        "El método no convergió después de {} iteraciones.".format(i))
