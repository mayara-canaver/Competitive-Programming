descarte = input()

lista = list(input().split())

lista2 = []

for palavra in lista:
    if len(palavra) == 3 and palavra[0] == "O" and palavra[1] == "B":
        lista2.append("OBI")
    elif len(palavra) == 3 and palavra[0] == "U" and palavra[1] == "R":
        lista2.append("URI")
    else:
        lista2.append(palavra)
        pass

print(" ".join(lista2))
