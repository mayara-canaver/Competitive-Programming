while True:
    vezes = int(input())
    aux, pico = 0, 0

    if vezes == 0:
        break

    lista = list(map(int, input().split()))
    if vezes == 2:
        if lista[0] != lista[1]:
            pico = 2
    else:
        for x in range(vezes):
            if x != 0 and x != vezes - 1:
                if lista[x-1] < lista[x] > lista[x+1]:
                    pico += 1
                elif lista[x-1] > lista[x] < lista[x+1]:
                    pico += 1
            else:
                if x == 0:
                    if lista[-1] < lista[x] > lista[x + 1]:
                        pico += 1
                    elif lista[-1] > lista[x] < lista[x + 1]:
                        pico += 1
                if x == vezes - 1:
                    if lista[x - 1] < lista[x] > lista[0]:
                        pico += 1
                    elif lista[x - 1] > lista[x] < lista[0]:
                        pico += 1

    print(pico)
