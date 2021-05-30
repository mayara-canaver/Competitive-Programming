vezes_feira = int(input())

for y in range(vezes_feira):
    total_frutas = int(input())
    soma = 0
    frutas = {}

    for x in range(total_frutas):
        fruta, valor = input().split()
        valor = float(valor)
        frutas[fruta] = valor

    qtd_frutas = int(input())

    for frutinha in range(qtd_frutas):
        fruta_ver, valor_ver = input().split()
        fruta_ver = float(frutas[fruta_ver])
        soma = soma + fruta_ver * int(valor_ver)

    print("R$ %.2f" % soma)
