x = int(input())
y = int(input())

if y > x:
    for numero in range(x + 1, y):
        if numero % 5 == 2 or numero % 5 == 3:
            print(numero)
elif x > y:
    for numero in range(y + 1, x):
        if numero % 5 == 2 or numero % 5 == 3:
            print(numero)
else:
    pass
