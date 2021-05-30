numeros = list(map(int, input().split()))
maximo = max(numeros)
a, b = numeros

if a == b:
    print(a)
else:
    print(maximo)
