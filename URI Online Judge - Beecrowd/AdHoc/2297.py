numero = 1

while True:
    casos = int(input())

    lst_aldo, lst_beto = [], []

    if numero != 1:
        print()
        
    if casos == 0:
        break

    for caso in range(casos):
        aldo, beto = list(map(int, input().split()))

        lst_aldo.append(aldo)
        lst_beto.append(beto)

    print("Teste %d" % numero)

    if sum(lst_aldo) > sum(lst_beto):
        print("Aldo")
    else:
        print("Beto")

    numero += 1
