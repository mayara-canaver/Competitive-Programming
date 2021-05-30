import sys

while True:
    numero = int(input())
    a1, a2 = 0, 1
    if numero == 0:
        sys.exit()
    for x in range(numero):
        a1, a2 = a2, (a1+a2)

    print(a2)