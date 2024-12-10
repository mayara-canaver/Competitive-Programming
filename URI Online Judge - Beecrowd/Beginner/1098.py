import sys

def bissexto(numero):
    return (numero%4 == 0 and numero%100 != 0) or  \
            (numero%4 == 0 and numero%400 == 0)

def huluculu(numero):
    return numero%15 == 0

def bulukulu(numero):
    return bissexto(numero) and numero%55 == 0

sep = ""

while True:
    try:
        soma = 0
        numero = int(input())
        print(sep, end="")
        sep = "\n"
        if bissexto(numero):
            print("This is leap year.")
            soma = soma + 1
        if huluculu(numero):
            print("This is huluculu festival year.")
            soma = soma + 1
        if bulukulu(numero):
            print("This is bulukulu festival year.")
            soma = soma + 1
        if soma == 0:
            print("This is an ordinary year.")

    except EOFError:
        sys.exit()