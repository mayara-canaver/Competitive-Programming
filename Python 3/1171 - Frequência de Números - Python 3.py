alunos, indice = list(map(int, input().split()))

lista = []

for x in range(alunos):
    aluno = input()
    lista.append(aluno)

lista = sorted(lista)
print(lista[indice - 1])
