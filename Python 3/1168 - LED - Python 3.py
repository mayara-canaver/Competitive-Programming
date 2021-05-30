import sys
try:
    while True:
        numero = input().split()
        numero = list(map(int, numero))
        v, t, d = numero[0], numero[1], 0
        d = v*(t*2)
        print("%d" %d)

except EOFError:
    sys.exit