def saldoRankeadas(vitorias, derrotas):
    saldo = vitorias - derrotas
    if (vitorias <= 10):
        nivel = "Ferro"
    elif (vitorias <= 20):
        nivel = "Bronze"
    elif (vitorias <= 50):
        nivel = "Prata"
    elif (vitorias <= 80):
        nivel = "Ouro"
    elif (vitorias <= 90):
        nivel = "Diamante"
    elif (vitorias <= 100):
        nivel = "Lendário"
    else:
        nivel = "imortal"
    return saldo, nivel

saldoVitorias, nivel = saldoRankeadas(70, 30)
print(f'O Herói tem saldo de {saldoVitorias} e está no nível de {nivel}')