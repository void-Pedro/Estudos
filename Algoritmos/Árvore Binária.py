class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    
    def altura(self, node):
        altEsquerda = 0
        altDireita = 0
        if node.left:
            altEsquerda = self.altura(node.left)
        if node.right:
            altDireita = self.altura(node.right)
        if altEsquerda == altDireita == 0:
            return 0
        if altEsquerda > altDireita:
            return altEsquerda + 1
        return altDireita + 1