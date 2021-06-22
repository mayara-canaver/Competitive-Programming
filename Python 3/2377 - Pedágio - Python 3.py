vezes = int(input())

horas = 0

for x in range(vezes):
    t, v = list(map(int, input().split()))
    horas += (t * v)

print(horas)
