def factorial(n, m):
    if (n <= 1):
        return 1
    else:
        return n * factorial(n - m, m)


vezes = int(input())

for vezezinha in range(vezes):
    qtd_ponto = 0
    numero = list(input())

    for caracter in numero:
        if caracter == "!":
            qtd_ponto += 1

    tamanho = len(numero) - qtd_ponto

    if qtd_ponto != 0:
        numero = numero[:tamanho]

    numerinho = int("".join(numero))

    print(factorial(numerinho, qtd_ponto))
