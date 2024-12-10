casos = int(input())

dicionario = {"bonecos": 0,
              "arquitetos": 0,
              "musicos": 0,
              "desenhistas": 0
              }

contador = 0

for caso in range(casos):
    nome, area, horas = list(input().split())
    horas = int(horas)

    dicionario[area] += horas

for chave, valores in dicionario.items():
    if chave == "bonecos":
        contador += valores // 8
    elif chave == "arquitetos":
        contador += valores // 4
    elif chave == "musicos":
        contador += valores // 6
    else:
        contador += valores // 12

print(contador)
