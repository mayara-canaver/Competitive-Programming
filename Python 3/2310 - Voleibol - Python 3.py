vezes = int(input())

for x in range(vezes):
    gols_r, gols_g, gols_b = 0, 0, 0
    gols = int(input())

    for j in range(gols):
        m, s = input().split()

        if m == "R":
            if s == "G":
                gols_r += 2
            elif s == "B":
                gols_r += 1

        if m == "G":
            if s == "B":
                gols_g += 2
            elif s == "R":
                gols_g += 1

        if m == "B":
            if s == "R":
                gols_b += 2
            elif s == "G":
                gols_b += 1

    listinha = [gols_r, gols_g, gols_b]
    maximo = max(listinha)
    listinha.remove(maximo)
    novo_maximo = max(listinha)

    if gols_r == gols_g == gols_b:
        print("trempate")
    elif maximo == novo_maximo:
        print("empate")
    else:
        if maximo == gols_r:
            print("red")
        elif maximo == gols_b:
            print("blue")
        elif maximo == gols_g:
            print("green")
