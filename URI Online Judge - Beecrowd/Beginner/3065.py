import re
num_caso = 1

while True:

    casos = int(input())

    if casos == 0:
        break
    else:

        expressao = input()

        lst_numeros = list(map(int, re.split(', |\+|-|!', expressao)))

        lst_operador = []

        total = 0

        for elemento in range(len(expressao)):
            if expressao[elemento] == "-":
                lst_operador.append("-")
            elif expressao[elemento] == "+":
                lst_operador.append("+")

        total = lst_numeros[0]

        del lst_numeros[0]

        for operador, numero in zip(lst_operador, lst_numeros):
            if operador == "+":
                total += numero
            else:
                total -= numero

        print("Teste %d" % num_caso)
        print(total)
        print()
        num_caso += 1
