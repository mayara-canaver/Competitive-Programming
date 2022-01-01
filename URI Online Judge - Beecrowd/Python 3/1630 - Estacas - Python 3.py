vezes = int(input())
x = 0
while x < vezes:

    numero = input().split()
    numero = list(map(int, numero))
    a, b = numero

    soma = 0

    if a > b:
        for y in range(b+1, a):
            if y%2 != 0:
                soma = soma + y

    else:
        for y in range(a+1, b):
            if y % 2 != 0:
                soma = soma + y

    print(soma)

    x = x + 1