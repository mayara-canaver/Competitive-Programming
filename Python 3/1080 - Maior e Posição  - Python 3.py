vezes = int(input())

for rotacao in range(vezes):
    numeros = input().split()
    numeros = list(map(int, numeros))
    x = numeros[0]
    y = numeros[1]
    r = pow(3*x, 2) + pow(y,2)
    b = 2*pow(x,2) + pow(5*y,2)
    c = -100*x + pow(y, 3)
    if (r>b and r>c):
        print("Rafael ganhou")
    elif (b>r and b>c):
        print("Beto ganhou")
    elif (c>b and c>r):
        print("Carlos ganhou")