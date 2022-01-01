vezes = int(input())

for x in range(vezes):
    gesto1 = input()
    gesto2 = input()
    if gesto1 == "pedra":
        if gesto2 == "ataque":
            print("Jogador 2 venceu")
        elif gesto2 == "pedra":
            print("Sem ganhador")
        else:
            print("Jogador 1 venceu")

    if gesto1 == "ataque":
        if gesto2 == "ataque":
            print("Aniquilacao mutua")
        elif gesto2 == "pedra":
            print("Jogador 1 venceu")
        else:
            print("Jogador 1 venceu")

    if gesto1 == "papel":
        if gesto2 == "ataque":
            print("Jogador 2 venceu")
        elif gesto2 == "pedra":
            print("Jogador 2 venceu")
        else:
            print("Ambos venceram")
