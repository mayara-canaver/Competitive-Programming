dicionario = {}

m, n = list(map(int, input().split()))

for x in range(m):
    valor1, valor2 = input().split()
    valor2 = int(valor2)
    dicionario[valor1] = valor2

for y in range(n):
    salario = 0
    while True:
        frase = input().split()
        if "." in frase:
            break
        for subfrase in frase:
            if subfrase in dicionario:
                salario = salario + dicionario.get(subfrase)

    print(salario)
