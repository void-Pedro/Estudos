class Pessoa:
    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome
        
    def nome_completo(self):
        print(f"Nome: {self.__nome}")
        
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)
        
    def nome_completo(self):
        print(f"Nome: {self._Pessoa__nome} a")
            
teste = Pessoa("Pedro", "Borges")
teste.nome_completo()
teste2 = Cliente("Jorge", "Amado")
teste2.nome_completo()