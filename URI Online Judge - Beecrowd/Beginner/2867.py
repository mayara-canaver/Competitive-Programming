def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


while True:
    try:
        vezes = int(input())

        for x in range(vezes):
            lista_secundaria = []
            lista_duende = list(map(int, input().split()))

            lista_duende.sort()

            for elemento in lista_duende:
                confere, auxiliar = True, elemento + 1

                while confere:
                    if gcd(elemento, auxiliar) == 1:
                        lista_secundaria.append(auxiliar)
                        confere = not confere
                    else:
                        auxiliar += 1

            print(max(lista_secundaria))

    except EOFError:
        break
