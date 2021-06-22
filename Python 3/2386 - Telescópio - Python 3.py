diametro = int(input())

c, l, a = list(map(int, input().split()))

if c >= diametro and l >= diametro and a >= diametro:
    print("S")
else:
    print("N")
