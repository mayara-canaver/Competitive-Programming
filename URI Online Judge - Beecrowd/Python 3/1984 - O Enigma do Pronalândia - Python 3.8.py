vezes = int(input())

dois, tres, quatro, cinco = 0, 0, 0, 0

numero = list(map(int, input().split()))
for x in numero:
    for y in range(2, 6):
        if x % y == 0:
            if y == 2:
                dois += 1
            if y == 3:
                tres += 1
            if y == 4:
                quatro += 1
            if y == 5:
                cinco += 1

print("%d Multiplo(s) de 2" % dois)
print("%d Multiplo(s) de 3" % tres)
print("%d Multiplo(s) de 4" % quatro)
print("%d Multiplo(s) de 5" % cinco)
