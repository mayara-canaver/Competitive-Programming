caracter = input()

texto = list(input().split())

count, total = 0, 0

for palavra in texto:

    if palavra.find(caracter) != -1:
        count += 1

porcent = (count / len(texto)) * 100

print("%.1f" % porcent)
