qtd_entrada = int(input())

for cenario in range(qtd_entrada):
    cenario += 1

    total_renas, rena_treno = list(map(int, input().split()))

    lst_rena = []

    for rena in range(total_renas):

        nome, peso, idade, altura = list(input().split())

        dict_rena = {"nome": nome,
                      "peso": peso,
                      "idade": idade,
                      "altura": altura}

        lst_rena.append(dict_rena)

    lst_rena = sorted(lst_rena, key=lambda dict_rena: (int(dict_rena["idade"]), float(dict_rena["altura"]), dict_rena["nome"]))

    lst_rena = sorted(lst_rena, key=lambda dict_rena: int(dict_rena["peso"]), reverse=True)

    lst_rena = lst_rena[: rena_treno]

    print("CENARIO {%d}" % cenario)

    rena = 0

    for treno in lst_rena:
        rena += 1
        print("%d - %s" % (rena, treno["nome"]))
