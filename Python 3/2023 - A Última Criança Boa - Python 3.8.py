lista = list(map(int, input().split()))

if lista[0] == lista[1] or lista[0] == lista[2] or lista[1] == lista[2]:
    print("S")
else:
    maximo = max(lista)
    lista.remove(maximo)

    if lista[0] + lista[1] == maximo:
        print("S")
    else:
        print("N")
