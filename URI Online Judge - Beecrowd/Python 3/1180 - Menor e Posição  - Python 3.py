vezes = int(input())

lista_par, lista_impar = [], []

for x in range(vezes):
    numero = int(input())
    if numero%2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

lista_par.sort()
lista_impar.sort()

lista_impar.reverse()

for i in lista_par:
    print(i)

for t in lista_impar:
    print(t)
