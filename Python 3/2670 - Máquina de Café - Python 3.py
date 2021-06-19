vezes = int(input())

for x in range(vezes):
    m, n = list(map(int, input().int()))
    m = jose, n = joao

    if m == 0:
        print(n + 1)

    elif n == 0 and m >= 1:
        n = 1
        print(m - 1)

    elif m >= 1 and n >= 1:
        print(m - 1)

    elif 0 < m <= 3:
        print(200)

    elif m == 4:
        n = 2

1    jose -> 0  -> n + 1
2    joao 0 and jose += 1 -> joao == 1 and jose == m - 1
3    joao += 1 and jose += 1 -> jose == m - 1
4    joao += 1 and jose += 1 -> joao= == m - 1
5    max(jose) == 3 -> max(joao) == 200
6    jose == 4 -> joao == 2


if m > 0 and n > 0:

    if 0 < m <= 3:
        n = 200
        print(n - 1)
    elif m == 4:
        n = 2
        valor = m - 1
        n - 1

    print(n-1)

então m pagaria o mesmo valor que teria que pagar caso m
propusesse m - 1 reais e n quisesse receber o mesmo que receberia se m propusesse m reais e ele pedisse n - 1 reais