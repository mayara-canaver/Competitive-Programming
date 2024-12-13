total_figurinhas = int(input())
compradas = int(input())

lista = []
tamanho = 0

for figurinha in range(compradas):
    figura = int(input())

    if figura not in lista:
        lista.append(figura)

tamanho = len(lista)

total_figurinhas -= tamanho

print(total_figurinhas)
