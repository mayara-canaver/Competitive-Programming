linha = int(input())

operacao = input()

tamanho_inicial = (linha) * 12
tamanho_final = (linha + 1) * 12

lista1 = []

for x in range(144):
    numerico = float(input())
    lista1.append(numerico)

lista2 = lista1[tamanho_inicial: tamanho_final]

if operacao == "S":
    principal = sum(lista2)
    print("%.1f" % principal)
else:
    principal = sum(lista2)/12
    print("%.1f" % principal)
