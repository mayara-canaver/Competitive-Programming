vezes = int(input())
anao, elfo, humano, mago, hobbit = 0, 0, 0, 0, 0

for x in range(vezes):
    nome, tipo = input().split()
    if tipo == "A":
        anao += 1
    if tipo == "E":
        elfo += 1
    if tipo == "H":
        humano += 1
    if tipo == "M":
        mago += 1
    if tipo == "X":
        hobbit += 1

print("%d Hobbit(s)" % hobbit)
print("%d Humano(s)" % humano)
print("%d Elfo(s)" % elfo)
print("%d Anao(s)" % anao)
print("%d Mago(s)" % mago)
