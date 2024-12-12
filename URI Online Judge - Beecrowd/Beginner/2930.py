vezes = int(input())
total = 0

for x in range(vezes):
    v1, v2 = input().split()
    v2 = int(v2)
    if v1 == "G":
        total -= v2
    else:
        total += v2

if total >= 0:
    print("A greve vai parar.")
else:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
