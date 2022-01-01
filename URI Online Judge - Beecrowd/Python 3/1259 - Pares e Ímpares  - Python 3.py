lista_par = []

for x in range(20):
    numero = int(input())
    lista_par.append(numero)

lista_par.reverse()

valor = 0

for i in lista_par:
    print("N[%d] = %d" % (valor, i))
    valor = valor + 1

