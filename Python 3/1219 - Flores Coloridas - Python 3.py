vezes = int(input())
x, coelho, rato, sapo, total, percecoelho, percenrato, percensapo = 0, 0, 0, 0, 0, 0, 0, 0

while x < vezes:
    frase = input().split()
    numero, caracter = frase
    numero = int(numero)

    if caracter == "C":
        coelho = coelho + numero
    if caracter == "R":
        rato = rato + numero
    if caracter == "S":
        sapo = sapo + numero

    total = total + numero

    x = x + 1

percecoelho = coelho/total*100
percenrato = rato/total*100
percensapo = sapo/total*100

print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % coelho)
print("Total de ratos: %d" % rato)
print("Total de sapos: %d" % sapo)
print("Percentual de coelhos: %.2f %%" % percecoelho)
print("Percentual de ratos: %.2f %%" % percenrato)
print("Percentual de sapos: %.2f %%" % percensapo)