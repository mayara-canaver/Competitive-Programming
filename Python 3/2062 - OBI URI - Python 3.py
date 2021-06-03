vezes = int(input())

for x in range(vezes):
    count = 0
    numero = int(input())

    for y in range(2, numero//2):
        if numero % y == 0:
            count += 1

    if numero == 1 or numero == 4:
        print("%d nao eh primo" % numero)
    elif count == 0 or numero == 2:
        print("%d eh primo" % numero)
    else:
        print("%d nao eh primo" % numero)