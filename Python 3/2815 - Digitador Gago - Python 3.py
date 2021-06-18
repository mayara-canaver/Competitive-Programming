texto = input().split()

lista = []

for palavra in texto:
    if palavra[:2] == palavra[2:4]:
        lista.append(palavra[2:])
    else:
        lista.append(palavra)

print(" ".join(lista))
