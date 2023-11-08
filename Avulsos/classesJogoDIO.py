class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    def atacar(self):
        if(self.tipo == "mago"):
            ataque = "magia"
        elif (self.tipo == "guerreiro"):
            ataque = "espada"
        elif (self.tipo == "monge"):
            ataque = "artes marciais"
        elif (self.tipo == "ninja"):
            ataque = "shuriken"
        print(f'O {self.tipo} atacou usando {ataque}')

pedro = Heroi("Pedro", 50, "mago")
pedro.atacar()