import scipy
import numpy as np

preto = 18
branco = 252

def geraMatriz(n):
    matriz = [[branco] * n for _ in range(n)]
    return matriz

img1 = geraMatriz(8)
for i in range (8):
    for j in range(4, 8):
        img1[i][j] = preto
#print(img1)

k = 1
img2 = geraMatriz(8)
for i in range(8):
    for j in range(k, 8, 2):
        img2[i][j] = preto
    k = (k+1)%2
#print (img2)

filtro = [[1/9, 1/9, 1/9],
          [1/9, 1/9, 1/9],
          [1/9, 1/9, 1/9]]  

img1conv = scipy.signal.convolve2d(img1, filtro, mode="full")
img2conv = scipy.signal.convolve2d(img2, filtro, mode="full")

print (img2conv)