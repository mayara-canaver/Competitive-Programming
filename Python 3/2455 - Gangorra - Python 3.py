lista_cartas = list(map(int, input().split()))

lista_cartas_decrescente = sorted(lista_cartas, reverse=True)

lista_cartas_crescente = sorted(lista_cartas)

if lista_cartas == lista_cartas_crescente:
    print("C")
elif lista_cartas == lista_cartas_decrescente:
    print("D")
else:
    print("N")
