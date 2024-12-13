while True:
    n, k, m = list(map(int, input().split()))
    lista = []
    funcionario1, funcionario2 = 0, 0

    if n == 0 and k == 0 and m == 0:
        break

    for pessoa in range(1, n+1):
        lista.append(pessoa)

    f2 = 0
    f1 = len(lista) - 1

    while len(lista) > 0:
        f1 = (f1 + k) % len(lista)

        f2 = (f2 - m) % len(lista)

        if lista[f1] == lista[f2]:
            print(f1)
            lista.pop(lista[f1])
            f1 = f1 % len(lista)
            f2 = (f2 - 1) % len(lista)
            f2 -= 1
        else:
            v1 = lista[f1]
            v2 = lista[f2]
            print(lista[f1])
            print(lista[f2])
            lista.pop(v1)
            lista.pop(v2)

