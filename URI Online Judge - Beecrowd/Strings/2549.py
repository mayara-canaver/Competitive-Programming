from sys import stdin

while True:
    inputo = stdin.readline()
    if not inputo:
        break

    n, a = list(map(int, inputo.split()))

    lst_alunos = []

    for aluno in range(n):
        aluno = list(stdin.readline().split())

        qtd = "".join([nome[0] for nome in aluno])
        lst_alunos.append(qtd)

    tamanho_inicial, tamanho_unicos = len(lst_alunos), len(set(lst_alunos))

    print(tamanho_inicial - tamanho_unicos)
