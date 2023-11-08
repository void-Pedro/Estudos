nome = "Pedro"
xp = 7500

if(xp <= 1000):
    nivel = "Ferro"
elif (xp <= 2000):
    nivel = "Bronze"
elif (xp <= 6000):
    nivel = "Prata"
elif (xp <= 7000):
    nivel = "Ouro"
elif (xp <= 8000):
    nivel = "Platina"
elif (xp <= 9000):
    nivel = "Ascendente"
elif (xp <= 10000):
    nivel = "Imortal"
else:
    nivel = "Radiante"
    
print(f'O herói de nome {nome} está no nível de {nivel}')