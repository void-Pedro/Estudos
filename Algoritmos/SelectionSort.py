# O Selection Sort é um algoritmo que funciona selecionando o menor valor (ou o maior, dependendo da orientação da ordenação), trocando-o de lugar com o valor que estava lá

def SelectionSort(A):
    n = len(A)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if(A[j] < A[minimo]):
                minimo = j
        A[i], A[minimo] = A[minimo], A[i]

vetor = [25, 10, 21, 11, 47, 1, 7, 26, 34]
SelectionSort(vetor)
print(vetor)