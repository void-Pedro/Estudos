# O algoritmo de Dijkstra é um dos algoritmos utilizados para o cálculo de caminhos mínimos entre vértices de um grafo. A partir de um vértice raiz, o algoritmo calcula
# a distância mínima até cada um dos outros vértices.
import heapq
INF = 99999

# Este algoritmo recebe como entrada um grafo ponderado G e um vértice inicial v (pertencente a G)
def Dijkstra(G, v):
    n = len(G)
    # Vetor para armazenar as distâncias mínimas a partir de um vértice
    distancias = [INF] * n
    # Vértice inicial tem distância 0
    distancias[v] = 0
    predecessores = [0] * n
    
    # Cria uma fila de prioridades com o vértice inicial com distância 0
    heap = [(0, v)]
    
    # Enquanto a fila de prioridade não estiver vazia
    while heap:
        # Pega o primeiro elemento da fila de prioridades (com menor distância)
        (distancia, verticeAtual) = heapq.heappop(heap)
        # Se a distância até o vértice atual for menor que a distância armazenada, pula para o próximo vértice
        if(distancia) > distancias[verticeAtual]:
            continue
        # Para cada vizinho do vértice atual
        for vizinho, w in G[verticeAtual]:
            distanciaAtual = distancia + w
            # Se a distância calculada for menor que a armazenada, atualiza a distância armazenada e adiciona esse vizinho ao heap
            if distanciaAtual < distancias[vizinho]:
                distancias[vizinho] = distanciaAtual
                predecessores[vizinho] = verticeAtual
                heapq.heappush(heap, (distanciaAtual, vizinho))
        # Retorna o vetor com todas as distâncias atualizadas
    return distancias, predecessores
    
grafo = [
    [(1, 2), (3, 1)],            # Vértice 0
    [(0, 2), (2, 3), (3, 1)],    # Vértice 1
    [(1, 3), (4, 2)],            # Vértice 2
    [(0, 1), (1, 1), (4, 1)],    # Vértice 3
    [(2, 2), (3, 1)]             # Vértice 4
]

distancias, predecessores = Dijkstra(grafo, 0)
print(distancias)
print(predecessores)