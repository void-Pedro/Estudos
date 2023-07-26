# def iguais(l1, l2):
#     qtdIguais = 0
#     n = len(l1)
    
#     for i in range(n):
#         for j in range(len(l2)):
#             if l1[i] == l2[j]:
#                 qtdIguais += 1
#                 l2.pop(j)
#                 break            
#     if qtdIguais == n:
#         return True
#     return False

def iguais(l1, l2):
    merge_sort(l1)
    merge_sort(l2)
    
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

def merge_sort(lista):
    
    if len(lista)>1:
        meio = int(len(lista)/2) # Índice do meio da lista
        E = lista[:meio] # Elementos à esquerda do meio
        D = lista[meio:] # Elementos à direita do meio (inclusive)
  
        merge_sort(E) # Ordenação da parte esquerda
        merge_sort(D) # Ordenação da parte direita
  
        i = 0
        j = 0
        k = 0
        
        while i < len(E) and j < len(D): 
            if E[i] < D[j]: 
                lista[k] = E[i] 
                i+=1
            else: 
                lista[k] = D[j] 
                j+=1
            k+=1
          
        while i < len(E): 
            lista[k] = E[i] 
            i+=1
            k+=1
          
        while j < len(D): 
            lista[k] = D[j] 
            j+=1
            k+=1

    

lista1 = [2, 6, 4, 8, 10, 3]
lista2 = [10, 3, 2, 4, 6, 8]
verdade = iguais(lista1, lista2)
print(verdade)