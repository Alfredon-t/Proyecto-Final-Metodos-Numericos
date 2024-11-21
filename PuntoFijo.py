import sympy as sp


def punto_fijo(f, g, x0, tol, max_iter):
    """
    Método de Punto Fijo.
    """
    iteraciones = 0
    error = float("inf")
    resultados = [(iteraciones, x0, None)]

    while error > tol and iteraciones < max_iter:
        x1 = g.subs(sp.Symbol('x'), x0)  # Sustituye el valor de x en g(x)
        error = abs(x1 - x0)  # Calcula el error
        resultados.append((iteraciones + 1, x1, error))
        if error < tol:
            return x1, resultados  # Retorna la raíz y las iteraciones
        x0 = x1
        iteraciones += 1

    # Si no converge
    return None, resultados
