# O algoritmo de Huffman é um algoritmo guloso utilizado para compressão de dados, gerando códigos binários de tamanho variável baseados na 
# frequência de ocorrência de cada símbolo (símbolos ou letras que mais aparecem terão um código binário menor, economizando espaço)
import heapq

# Dado um dicionário com os símbolos e probabilidades, o algoritmo abaixo cria uma árvore de Huffman
def arvoreHuffman(tabela):
    # Cria um vetor para armazenar os elementos do heap
    heap = []
    # "Traduz" o dicionário com as probabilidades, adicionando os nós criados no vetor de heap
    for simbolo, prob in tabela.items():
        heapq.heappush(heap, (prob, simbolo))

    # Enquanto o heap não tiver apenas um elemento (raíz), 
    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)

        # Cria uma subárvore contendo as duas menores frequências e adiciona no vetor heap
        z = ((x[0] + y[0]),"", x, y)
        heapq.heappush(heap, z)

    raiz = heapq.heappop(heap)
    return raiz
    
# Transcreve, de forma recursiva, a árvore em um código de Huffman
def codHuffman(nodo, codAtual, codigo):
    # Se o nó for folha (sem filhos), vincular o código atual ao símbolo
    if len(nodo) == 2:
        simb = nodo[1]
        codigo[simb] = codAtual
        # Se não for, realizar o mesmo processo pros filhos, adicionando 0 ao código do filho da esquerda e 1 ao código do da direita
    else:
        codHuffman(nodo[2], codAtual + "0", codigo)
        codHuffman(nodo[3], codAtual + "1", codigo)
    
tabela_port = {
    "a": 14.63,
    "b": 1.04,
    "c": 3.88,
    "d": 4.99,
    "e": 12.57,
    "f": 1.02,
    "g": 1.30,
    "h": 1.28,
    "i": 6.18,
    "j": 0.40,
    "k": 0.02,
    "l": 2.78,
    "m": 4.74,
    "n": 5.05,
    "o": 10.73,
    "p": 2.52,
    "q": 1.20,
    "r": 6.53,
    "s": 7.81,
    "t": 4.34,
    "u": 4.63,
    "v": 1.67,
    "w": 0.01,
    "x": 0.21,
    "y": 0.01,
    "z": 0.47
}

tabela_ing = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074
}

# Cria as árvores de Huffman para os dois dicionários de valores
raizPort = arvoreHuffman(tabela_port)
raizIng = arvoreHuffman(tabela_ing)

# Transcrição da árvore para binário
codigoPort = {}
codigoIng = {}
codAtualP = ""
codAtualI = ""
codHuffman(raizPort, codAtualP, codigoPort)
codHuffman(raizIng, codAtualI, codigoIng)

# Calcula o tamanho médio do código da forma tradicional e usando Huffman para o dicionário em português
# OBS: este tamanho médio está para um código com 100 caracteres, já que foi apenas dado a frequência
custoTotalPort = 0
for simbolo, freq in tabela_port.items():
    custoTotalPort += freq * 5

custoHuffmanPort = 0
for simbolo, cod in codigoPort.items():
    custoHuffmanPort += len(cod) * tabela_port.get(simbolo)

# Calcula qual a porcentagem que o código de Huffman economizou
economiaPort = (1 - (custoHuffmanPort / custoTotalPort)) * 100

# Printa a tabela dos código e a comparação entre os métodos
print("***** Comparação para o dicionário em português *****")
print(f"Custo do método tradicional: {custoTotalPort:,.2f}")
print(f"Custo utilizando Huffman:  {custoHuffmanPort:,.2f}")
print(f"Espaço economizado: {economiaPort:,.1f}%")
print("Tabela dos códigos de Huffman:")
for simb, cod in sorted(codigoPort.items()):
    print(simb, ": ", cod)

# Calcula o tamanho médio do código da forma tradicional e usando Huffman para o dicionário em inglês
custoTotalIng = 0
for simbolo, freq in tabela_ing.items():
    custoTotalIng += freq * 5   

custoHuffmanIng = 0
for simbolo, cod in codigoIng.items():
    custoHuffmanIng += len(cod) * tabela_ing.get(simbolo)

# Calcula qual a porcentagem que o código de Huffman economizou
economiaIng = (1 - (custoHuffmanIng / custoTotalIng)) * 100

# Printa a tabela dos código e a comparação entre os métodos
print("***** Comparação para o dicionário em português *****")
print(f"Custo do método tradicional: {custoTotalIng:,.2f}")
print(f"Custo utilizando Huffman:  {custoHuffmanIng:,.2f}")
print(f"Espaço economizado: {economiaIng:,.1f}%")
print("Tabela dos códigos de Huffman:")
for simb, cod in sorted(codigoIng.items()):
    print(simb, ": ", cod)