q, e = list(map(int, input().split()))

escritorios = list(map(int, input().split()))

for x in range(q):
    sala = int(input())

    if sala in escritorios:
        print(0)
    else:
        print(1)
        escritorios.append(sala)
