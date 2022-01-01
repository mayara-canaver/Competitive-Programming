vezes = int(input())

for x in range(vezes):
    s = 0
    numero = int(input())
    for y in range(1, (numero//2) + 1):
        if numero % y == 0:
            s += y
    if s == numero:
        print("%d eh perfeito" % numero)
    else:
        print("%d nao eh perfeito" % numero)