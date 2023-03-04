# Os algoritmos de Kruskal e Primm utilizam da abordagem gulosa para construír árvores geradoras mínimas
# O Kruskal escolhe, a cada passo, a aresta de menor heurística (sem que se formem cíclos).

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

