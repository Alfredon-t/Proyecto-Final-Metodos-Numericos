import sympy as sp


def punto_fijo(f, g, x0, tol, max_iter):
    """
    Método de Punto Fijo que calcula la raíz de f(x) usando g(x).
    Incluye f(x) en los resultados.
    """
    iteraciones = 0
    error = float("inf")
    # Agregar f(x) evaluado en x0
    resultados = [(iteraciones, x0, None, f.subs(sp.Symbol('x'), x0))]

    while error > tol and iteraciones < max_iter:
        x1 = g.subs(sp.Symbol('x'), x0)  # Sustituye el valor de x en g(x)
        error = abs(x1 - x0)  # Calcula el error
        f_valor = f.subs(sp.Symbol('x'), x1)  # Evalúa f(x) en el nuevo x
        resultados.append((iteraciones + 1, x1, error, f_valor))

        if error < tol:
            return x1, resultados  # Retorna la raíz y las iteraciones

        x0 = x1  # Actualiza x0
        iteraciones += 1

    return None, resultados  # Si no converge
