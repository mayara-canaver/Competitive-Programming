from sys import stdin

casos = int(stdin.readline().strip())

for caso in range(casos):
    p_1 = input()
    p_2 = input()

    p_final = input()

    lst_pos = []

    for letra in range(len(p_final)):
        if p_final[letra] == "_":
            lst_pos.append(letra)

    if p_1[lst_pos[0]] == p_2[lst_pos[1]] or p_1[lst_pos[1]] == p_2[lst_pos[0]]:
        print("Y")
    else:
        print("N")
