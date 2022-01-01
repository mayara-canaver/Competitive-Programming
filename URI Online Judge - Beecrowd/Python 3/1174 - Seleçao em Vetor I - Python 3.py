vezes = int(input())
aux, prox = 0, 1
for x in range(vezes):
    print('%d ' % aux if x != vezes - 1 else '%d' % aux, end='')
    prox, aux = prox + aux, prox

print()
