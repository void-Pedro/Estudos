import numpy

def f(x):
    # Defina a função que deseja integrar aqui
    return x**2

def simpson_integral(a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)

    for i in range(2, n-1, 2):
        integral += 2 * f(a + i * h)

    integral *= h / 3
    return integral

# Intervalo de integração
a = -1,2
b = 2,2

# Número de subintervalos (deve ser um número ímpar)
n = 10000

integral_value = simpson_integral(a, b, n)
print(f"O valor numérico da integral é: {integral_value:.8f}")