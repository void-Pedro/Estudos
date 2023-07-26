import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread(r'C:\Users\pedro\desktop\imagem2.jpg', cv2.IMREAD_GRAYSCALE)
npixels = imagem.shape[0] * imagem.shape[1]

plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap='gray')

# Cria um vetor a[i] com 256 posições para armazenar a quantidade de pixels com tom de cinza igual a i
def criarHist():
    a = []
    for i in range(0, 256):
        a.append(0)
        
    return a

# Função para normalizar o histograma
def normalizar(hist, tamanho):
    for i in range(0, 256):
        hist[i] = hist[i] / tamanho

# Percorre todos os pixels na imagem e, para cada um, adiciona uma unidade ao valor do vetor no índice correspondente ao seu tom de cinza
def contarIntensidade(hist, img):
    for i in img:
        for j in i:
            hist[j] = hist[j] + 1

# Cria o histograma da imagem, preenchendo com a frequência de cada nível de cinza
hist = criarHist()
contarIntensidade(hist, imagem)

# Cria um vetor de probabilidade para cada nível de cinza
vetProb = []
for i in range(0, 256):
    vetProb.append(hist[i]/npixels)
    
# Normaliza o histograma
normalizar(hist, npixels)

# Melhor limiar e melhor variância encontradas (limiar que gera a menor variância)
mlimiar = 0
mvariancia = 0

# Esta seção verifica cada limiar no intervalo de 0 a 256, para achar o que minimiza a variância intraclasse
for limiar in range(0, 256):
    
    # Calcula a probabilidade de estar menor ou maior que o limiar
    probMenor = np.sum(hist[:limiar])
    probMaior = np.sum(hist[limiar:])
    
    # Calcula a média da intensidade dos valores menores e maiores que o limiar
    if(probMenor == 0):
        mediaMenor = 0
    else:
        mediaMenor = np.sum(hist[:limiar] * limiar) / probMenor
        
    if(probMaior == 0):
        mediaMaior = 0
    else:
        mediaMaior = np.sum(hist[limiar:] * limiar) / probMaior
    
    variancia = probMenor*probMaior * (mediaMaior - mediaMenor)**2
    
    # Se a variância calculada for maior que a melhor variância, este será o novo melhor limiar e esta será a melhor variância
    if variancia > mvariancia:
        mlimiar = limiar
        mvariancia = variancia

# Binariza a imagem para branco e preto pelo valor do melhor limiar encontrado
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if (imagem[i][j] < mlimiar):
            imagem[i][j] = 0
        else:
            imagem[i][j] = 255

plt.subplot(1, 2, 2)
plt.imshow(np.squeeze(imagem), cmap='gray')
plt.show()