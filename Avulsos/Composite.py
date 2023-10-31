class Objeto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Caixa:
    def __init__(self, nome):
        self.nome = nome
    
    conteudo = []
    def add(self, obj):
        self.conteudo.append(obj)
        
    def showContent(self):
        print("Esta é a caixa", self.nome)
        for item in conteudo:
            print(item.nome)

b = Caixa(1)
obj1 = Objeto(1, 35)
b.add(obj1)
b.showContent()

        
    
