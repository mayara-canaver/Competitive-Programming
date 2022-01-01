altura, canos = list(map(int, input().split()))

lista = list(map(int, input().split()))
count = 0

for item in range(len(lista) - 1):
    if abs(lista[item] - lista[item + 1]) <= altura:
        pass
    else:
        count += 1

if count > 0:
    print("GAME OVER")
else:
    print("YOU WIN")
