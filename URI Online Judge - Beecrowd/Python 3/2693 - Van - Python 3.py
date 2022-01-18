while True:
    try:
        qtd_entrada = int(input())

        lst_aluno = []

        for aluno in range(qtd_entrada):

            nome, regiao, custo = list(input().split())

            dict_aluno = {"nome": nome,
                          "regiao": regiao,
                          "custo": custo}

            lst_aluno.append(dict_aluno)

        lst_aluno = sorted(lst_aluno, key=lambda dict_aluno: (int(dict_aluno["custo"]), dict_aluno["regiao"], dict_aluno["nome"]))

        print("\n".join([aluno["nome"] for aluno in lst_aluno]))

    except EOFError:
        break
