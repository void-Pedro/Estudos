import scipy
import numpy as np

matriz = [[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]]

filtro = [[1, 2, 1],
          [2, 4, 2],
          [1, 2, 1]]

A = scipy.signal.convolve2d(matriz, filtro, mode="full", boundary="fill")
print(A)