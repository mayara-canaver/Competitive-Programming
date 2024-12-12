n, g = list(map(int, input().split()))

dicionario = {}

for numero in range(n):
    ri, vi = input().split()
    dicionario[ri] = int(vi)

qtd = int(input())
lista = list(input().split())

contador = 0

for elemento in lista:
    if elemento in dicionario.keys():
        contador += dicionario.get(elemento)

print(contador)

if contador >= g:
    print("You shall pass!")
else:
    print("My precioooous")
