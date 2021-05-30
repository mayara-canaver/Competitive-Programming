numeros = list(map(int, input().split()))
a, b = numeros[0], numeros[1]
soma, indexo = 0, 1

while True:
    if b > 0:
        for x in range(b):
            soma = soma + a + x
        break
    else:
        indexo += 1
        b = numeros[indexo]

print(soma)