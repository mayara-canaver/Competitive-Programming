from math import pow

numero = 1

while True:
    cortes = int(input())

    if numero != 1:
        print()

    if cortes == -1:
        break

    print("Teste %d" % numero)
    print(int(pow((pow(2, cortes) + 1), 2)))

    numero += 1
