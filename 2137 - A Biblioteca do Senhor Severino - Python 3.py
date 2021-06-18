lista_vogal = ["a", "e", "i", "o", "u"]

lista_final = []

risada = input()

for caracter in risada:
    if caracter in lista_vogal:
        lista_final.append(caracter)

lista_final_final = lista_final.copy()

lista_final_final.reverse()

if lista_final == lista_final_final:
    print("S")
else:
    print("N")
