import sympy as sp

def newton_raphson(f_evaluar, var, x0, tol=1e-6, i=100): #i es el número de iteraciones
    f_prima = sp.diff(f_evaluar, var)
    f = sp.lambdify(var, f_evaluar)
    f_derivative = sp.lambdify(var, f_prima)
    
    x_n = x0
    for i in range(i):
        fx_n = f(x_n)
        f_prime_x_n = f_derivative(x_n)
        
        if abs(f_prime_x_n) < 1e-10:  #usamos 1e-10 para representar a 0
            raise ValueError("Error. La función no se puede evaluar")
        
        x_next = x_n - (fx_n / f_prime_x_n) #Formula de Newton-Raphson
        
        if abs(x_next - x_n) < tol:
            return x_next
        
        x_n = x_next
    
    raise ValueError("El método no convergió después de {} iteraciones.".format(i))