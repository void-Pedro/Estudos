


def lagrange_interpolation(x_values, y_values, x):
    """
    Realiza a interpolação de grau 2 usando o polinômio de Lagrange.

    Parâmetros:
    - x_values: Lista dos valores de x conhecidos.
    - y_values: Lista dos valores de y conhecidos correspondentes aos valores de x.
    - x: O ponto no qual a interpolação deve ser calculada.

    Retorna:
    - O valor interpolado em x.
    """

    if len(x_values) != 4 or len(y_values) != 4:
        raise ValueError("A interpolação de grau 2 requer exatamente 3 pontos.")

    result = 0.0

    for i in range(3):
        term = y_values[i]
        for j in range(3):
            if i != j:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

# Exemplo de uso:
x_values = [0.7, 0.8, 0.9, 1]
y_values = [0.6006856, 0.6576698, 0.7062415, 0.746821]

x_interpolate = 0.85
result = lagrange_interpolation(x_values, y_values, x_interpolate)
print(f'O valor interpolado em x={x_interpolate} é {result}')