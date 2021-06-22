import operator

quantidade_alunos, times = list(map(int, input().split()))

lista_alunos = []
dicionario = {}

for aluno in range(quantidade_alunos):
    nome, habilidade = list(input().split())
    habilidade = int(habilidade)
    dicionario[nome] = habilidade

for aluno in range(quantidade_alunos):
    habilidade_maxima = max(dicionario.items(), key=operator.itemgetter(1))[0]
    lista_alunos.append(habilidade_maxima)
    del dicionario[habilidade_maxima]

numero_time = 1

while len(lista_alunos) > 0:
    print("Time %d" % numero_time)
    for aluninho in lista_alunos[::times]:
        print(aluninho)
        lista_alunos.remove(aluninho)

    numero_time += 1
    print()
