def retorna_valor(ataque, defesa, nivel, bonus):
    if nivel % 2 == 0:
        formula = (ataque + defesa) / 2 + bonus
    else:
        formula = (ataque + defesa) / 2

    return formula

vezes = int(input())

for x in range(vezes):
    bonus = int(input())
    ataque1, defesa1, nivel1 = list(map(int, input().split()))
    dabriel = retorna_valor(ataque1, defesa1, nivel1, bonus)
    ataque2, defesa2, nivel2 = list(map(int, input().split()))
    guarte = retorna_valor(ataque2, defesa2, nivel2, bonus)

    if dabriel > guarte:
        print("Dabriel")
    elif guarte > dabriel:
        print("Guarte")
    else:
        print("Empate")
