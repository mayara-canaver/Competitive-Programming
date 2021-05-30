import math

def mdc_funcao(soma1, soma2):
    if(soma2 == 0):
        return soma1
    else:
        return mdc_funcao(soma2, soma1 % soma2)

numero = int(input())

for i in range(numero):
    soma1, soma2 = 0, 0
    expressao = input().split()
    n1, n2, n3, n4 = int(expressao[0]), int(expressao[2]), int(expressao[4]), int(expressao[6])
    c2 = expressao[3]
    if c2 == "+":
        soma1 = (n1 * n4 + n3 * n2)
        soma2 = (n2 * n4)
    if c2 == "-":
        soma1 = (n1 * n4 - n3 * n2)
        soma2 = (n2 * n4)
    if c2 == "*":
        soma1 = (n1 * n3)
        soma2 = (n2 * n4)
    if c2 == "/":
        soma1 = (n1 * n4)
        soma2 = (n3 * n2)

    print("%d/%d = " % (soma1, soma2), end="")

    mdc = mdc_funcao(soma1, soma2)

    soma1 = soma1/mdc

    soma2 = soma2/mdc

    print("%d/%d" % (soma1, soma2))
