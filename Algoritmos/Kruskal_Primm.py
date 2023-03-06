# Os algoritmos de Kruskal e Primm utilizam da abordagem gulosa para construír árvores geradoras mínimas
# O Kruskal adiciona cada vértice como raíz de uma árvore e adicionando as arestas de menor custo com 
# extremidades em árvores distintas (usando a função unir)
# O algoritmo de Primm, por sua vez, inicia de uma raíz e, a cada passo, adiciona a aresta de menor
#  custo com uma extremidade nos vértices visitados e outra nos não visitados
import heapq
INF = 9999999

class GrafoKruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    # U e V são os nós e W a heurística
    def add_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

    # Função utilizada para 
    def find(self, p, i):
        if p[i] is not i:
            p[i] = self.find(p, p[i])
        return p[i]

    # Une, por nível, os elementos de dois conjuntos x e y
    def unir(self, p, nivel, x, y):
        
        if nivel[x] < nivel[y]:
            p[x] = y
        elif nivel[x] > nivel[y]:
            p[y] = x
        else: # Mesmo nível da árvore
            p[y] = x
            nivel[x] += 1

    def Kruskal(self):
        # Armazena a árvore mínima
        mst = []

        # Variáveis de índices, em que o i será utilizada
        # nas arestas e j no índice da MST
        i = 0
        j = 0

        # Ordena as arestas do grafo pelo seu peso de forma parecida
        # com uma fila de prioridade
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        
        # Lista para armazenar os "pais" dos nós
        p = []
        nivel = []

        # Define os pais e o nível de cada nó
        for node in range(self.V):
            p.append(node)
            nivel.append(0)

        # Para cada vértice
        while j < self.V-1:
            
            # Acha a aresta com o menor peso
            u, v, w = self.grafo[i]
            x = self.find(p, u)
            y = self.find(p, v)
            i += 1

            # Se não causar um cíclo, adiciona a aresta na MST
            if x != y:
                mst.append([u, v, w])
                self.unir(p, nivel, x, y)
                j += 1

        # Printa as arestas da árvore mínima e o custo total do caminho
        custoMin = 0
        print("Arestas da MST (Kruskal)")
        for u, v, w in mst:
            custoMin += w
            print("%d--%d = %d" % (u+1, v+1, w))
        print("Custo: ", custoMin)

def prim(graph, inicio):
    heap = [(0, inicio)]
    visitados = set()
    caminho = []
    custoTotal = 0

    while heap:
        (w, v) = heapq.heappop(heap)

        if v not in visitados:
            visitados.add(v)
            caminho.append(v)
            custoTotal += w

            for vizinho, vw in graph[v]:
                if vizinho not in visitados:
                    heapq.heappush(heap, (vw, vizinho))

    return (custoTotal, caminho)
   

# Exemplo do algoritmo de kruskal em um grafo ponderado
# Grafo utilizado: https://old.scielo.br/img/revistas/pope/v27n1/a08fig01.gif    
g = GrafoKruskal(5)
g.add_aresta(0, 1, 35)
g.add_aresta(0, 2, 40)
g.add_aresta(1, 2, 25)
g.add_aresta(1, 3, 10)
g.add_aresta(2, 3, 20)
g.add_aresta(2, 4, 15)
g.add_aresta(3, 4, 30)
g.Kruskal()

grafo = {
    '1': [('2', 35), ('3', 40)],
    '2': [('1', 35), ('3', 25), ('4', 10)],
    '3': [('1', 40), ('2', 25), ('4', 20), ('5', 15)],
    '4': [('2', 10), ('3', 20), ('5', 30)],
    '5': [('3', 15), ('4', 30)]
}

custo, caminho = prim(grafo, '1')
print(f'MST: {caminho}')
print(f'Custo total: {custo}')