numero = input()

c_zero, c_um = 0, 0

for caracter in numero:
    if caracter == "1":
        c_um += 1

if c_um % 2 == 0:
    numero = numero + "0"

else:
    numero = numero + "1"

print(numero)