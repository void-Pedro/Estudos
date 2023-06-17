import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread(r'C:\Users\pedro\desktop\imgteste.tiff', cv2.IMREAD_GRAYSCALE)

# Cria um vetor a[i] com 256 posições para armazenar a quantidade de pixels com tom de cinza igual a i
def criarHist():
    a = []
    for i in range(0, 256):
        a.append(0)
        
    return a

# Percorre todos os pixels na imagem e, para cada um, adiciona uma unidade ao valor do vetor no índice correspondente ao seu tom de cinza
def contarIntensidade(hist, img):
    for i in img:
        for j in i:
            hist[j] = hist[j] + 1

# Esta função cria um vetor para armazenar a soma das probabilidades acumuladas para cada nível de cinza
def somaAcumulada(prob):
    pacumulada = []
    probtotal = 0
    
    for i in range(0, 256):
        if i == 0:
            pacumulada.append(0)
            pass
        else:
            probtotal += prob[i-1]
        pacumulada.append(prob[i] + probtotal)
    return pacumulada

def equalizar(imagem):
    # Plota a imagem original
    plt.subplot(1, 2, 1)
    plt.imshow(imagem, cmap='gray')
    
    # Chama as funções para criar um histograma vazio, preenchendo com a frequência dos níveis de cinza
    hist = criarHist()
    contarIntensidade(hist, imagem)
    
    # Cria um vetor para armazenar a probabilidade para cada nível de cinza
    npixels = imagem.shape[0] * imagem.shape[1]
    vetProb = []
    for i in range(0, 256):
        vetProb.append(hist[i]/npixels)
    #print (vetProb)
    
    # Cria um vetor para armazenar a soma acumulada, armazenando em um vetor que será utilizado para fazer a transformação da imagem
    probAcumulada = somaAcumulada(vetProb)
    novaImg  = []
    for i in range(0, 256):
        novaImg.append(np.ceil(probAcumulada[i]*255))
        
    # Transforma a imagem original
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            imagem[i][j] = novaImg[imagem[i][j]]
    
    # Plota na tela a imagem
    plt.subplot(1, 2, 2)
    plt.imshow(np.squeeze(imagem), cmap='gray')
    plt.show()

equalizar(imagem)