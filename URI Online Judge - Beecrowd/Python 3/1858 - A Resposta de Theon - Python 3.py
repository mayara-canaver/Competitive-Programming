qt = int(input())

for i in range(qt):
    nome1, x1, nome2, x2 = input().split()
    numeros = list(map(int, input().split()))
    n1, n2 = numeros
    soma = n1 + n2
    if x1 == "PAR":
        if soma%2 == 0:
            print(nome1)
        else:
            print(nome2)
    else:
        if soma%2 == 0:
            print(nome2)
        else:
            print(nome1)
