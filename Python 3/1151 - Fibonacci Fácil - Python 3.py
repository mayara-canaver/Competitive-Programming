vezinha = int(input())
for x in range(vezinha):
    vezes = int(input())
    aux, prox = 0, 1
    if vezes == 0:
        print("Fib(0) = 0")
    for y in range(vezes):
        prox, aux = prox + aux, prox
        if y == vezes - 1:
            print("Fib(%d) = %d" % (vezes, aux))
