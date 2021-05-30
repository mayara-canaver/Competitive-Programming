coluna = int(input())

operacao = input()

matriz = []

for x in range(0, 12, 1):
    linha = []
    for y in range(0, 12, 1):
        x_num = float(input())
        linha.append(x_num)
    matriz.append(linha)

soma = [linha[coluna] for linha in matriz]

if operacao == "S":
    principal = sum(soma)
    print("%.1f" % principal)
else:
    principal = sum(soma)/12
    print("%.1f" % principal)


