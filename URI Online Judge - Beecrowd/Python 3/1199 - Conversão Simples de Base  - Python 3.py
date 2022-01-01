vezes = int(input())


for x in range(vezes):
    diagonais = input().split()
    diagonais = list(map(int, diagonais))
    d1, d2 = diagonais[0], diagonais[1]
    resultado = (d1*d2)/2
    print("%d cm2" %resultado)