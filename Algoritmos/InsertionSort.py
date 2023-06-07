# O Insertion Sort é um algoritmo de ordenação que funciona percorrendo a lista e, à medida que avança, vai deixando os elementos à esquerda do índice ordenados

def InsertionSort(A):
    n = len(A)
    for i in range(n):
        for j in range(i):
            if(A[j] < A[i]):

vetor = [25, 10, 21, 11, 47, 1, 7, 26, 34]