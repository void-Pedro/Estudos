import sympy as sp

# Definindo a variável simbólica
x = sp.symbols('x')

# Definindo a função
f = sp.exp(-(x/2.07)**2)

# Calculando a terceira derivada
f_third_derivative = sp.diff(f, x, 3)

# Encontrando o valor máximo da terceira derivada no intervalo [0, 1]
max_third_derivative = max([abs(f_third_derivative.subs(x, xi)) for xi in [0, 1]])

print(f'O valor máximo da terceira derivada no intervalo [0, 1] é: {max_third_derivative}')

# Função para calcular f(x)
f_func = sp.lambdify(x, f)

# Criando a tabela de valores
x_values = [0, 1/2, 1]
table = [(xi, f_func(xi)) for xi in x_values]

print("Tabela de valores (x, f(x)):")
for row in table:
    print(row)

# Criando o polinômio interpolador de grau 2
p2 = sp.lagrange(x_values, [f_func(xi) for xi in x_values])

# Expandindo o polinômio interpolador completamente
p2_expanded = sp.expand(p2)
print(f'O polinômio interpolador p2(x) é: {p2_expanded}')

# Calculando a integral de f(x)
integral_f = sp.integrate(f, (x, 0, 1))

# Calculando a integral do polinômio interpolador p2(x)
integral_p2 = sp.integrate(p2, (x, 0, 1))

print(f'A integral de f(x) é aproximadamente: {integral_f.evalf()}')
print(f'A integral de p2(x) é aproximadamente: {integral_p2.evalf()}')
