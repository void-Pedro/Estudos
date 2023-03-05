# Os algoritmos de Kruskal e Primm utilizam da abordagem gulosa para construír árvores geradoras mínimas
# O Kruskal escolhe, a cada passo, a aresta de menor heurística (sem que se formem cíclos).
from igraph import *

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    #U e V são os nós e W a heurística
    def add_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

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
        mst = []
        i = 0
        j = 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        p = []
        nivel = []
        for node in range(self.V):
            p.append(node)
            nivel.append(0)

        while j < self.V-1:
            u, v, w = self.grafo[i]
            i += 1
            x = self.find(p, u)
            y = self.find(p, v)

            if x != y:
                j += 1
                mst.append([u, v, w])
                self.unir(p, nivel, x, y)

        custoMin = 0
        print("Arestas da MST")
        for u, v, w in mst:
            custoMin += w
            print("%d--%d = %d" % (u, v, w))
        print("MST", custoMin)
    
g = Grafo(5)
g.add_aresta(0, 1, 35)
g.add_aresta(0, 2, 40)
g.add_aresta(1, 2, 25)
g.add_aresta(1, 3, 10)
g.add_aresta(2, 3, 20)
g.add_aresta(2, 4, 15)
g.add_aresta(3, 4, 30)
g.Kruskal()