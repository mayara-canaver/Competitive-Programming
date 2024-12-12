lista_apostados = list(map(int, input().split()))
lista_sorteados = list(map(int, input().split()))

count = 0

for numero in lista_apostados:
    if numero in lista_sorteados:
        count += 1

if count == 3:
    print("terno")
elif count == 4:
    print("quadra")
elif count == 5:
    print("quina")
elif count == 6:
    print("sena")
else:
    print("azar")
