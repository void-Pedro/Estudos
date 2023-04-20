# O BubbleSort é um algoritmo de ordenação que funciona varrendo o vetor n vezes e, para cada item, verifica se é maior que o próximo. 
# Se for, troca-os de lugar, ordenando o vetor de forma crescente (A[0] < A[n])
def BubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(n-i-1):
            if (A[j] > A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
    return

vetor = [25, 10, 21, 11, 47, 1, 7, 26, 34]
BubbleSort(vetor)
print(vetor)
