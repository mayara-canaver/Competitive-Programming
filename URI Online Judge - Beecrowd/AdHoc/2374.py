area = int(input())
estrelas = int(input())
count = 0

for fluxo in range(estrelas):
    foton = int(input())
    if foton * area >= 40000000:
        count += 1

print(count)
