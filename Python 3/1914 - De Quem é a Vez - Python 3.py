qt = int(input())

for i in range(qt):
    frase = input().split()
    lista = list(sorted(frase, key=len, reverse=True))
    print(*lista)
