vezes = int(input())
lista_f, lista_m = [], []

for x in range(vezes):
    nome, sexo = input().split()

    if sexo == "M":
        lista_m.append(sexo)
    else:
        lista_f.append(sexo)

print("%d carrinhos" % len(lista_m))
print("%d bonecas" % len(lista_f))
