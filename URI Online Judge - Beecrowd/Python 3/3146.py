count = 0
jipe = 0

while True:
    frase = list(input().split())

    if frase[0] == "ABEND":
        print(count)
        print(jipe)
        break

    palavra, numero = frase[0], frase[1]

    numero = int(numero)

    if palavra == "SALIDA":
        count += numero
        jipe += 1
    else:
        count -= numero
        jipe -= 1
