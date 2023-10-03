# Implementação do filtro de Wiener adaptativo pontual, realizado como a 3ª tarefa prática da matéria de Processamento de Imagens Digitais

import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

imagem = cv2.imread("desktop/imagens/boat.tif", cv2.IMREAD_GRAYSCALE)
plt.imshow(imagem)

def filtroWiener(imagem, tamJanela, varRuido):
    # Normalizando a imagem
    max = np.max(imagem)
    imagem = imagem / max
    
    larguraImg = imagem.shape[0]
    alturaImg = imagem.shape[1]        
    
    imagemFiltrada = np.zeros_like(imagem)
    
    for y in range(alturaImg):
        for x in range(larguraImg):
            janela = imagem[max(y-tamJanela // 2, 0):min(y + tamJanela // 2 + 1, alturaImg),
                            max(x-tamJanela // 2, 0):min(x + tamJanela // 2 + 1, larguraImg)]   
            mediaLocal = np.mean(janela)
            varianciaLocal = np.var(janela)
            
            imagemFiltrada[y, x] = mediaLocal + (varianciaLocal - varRuido) / (varianciaLocal + varRuido) * (imagem[y, x] - mediaLocal)
            
    return imagemFiltrada