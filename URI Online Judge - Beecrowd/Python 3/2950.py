while True:
    numeros = input().split()
    numeros = list(map(int, numeros))
    x, m = numeros
    if x == m == 0:
        break
    print(x*m)