import sys
while True:

    numero = int(input())
    if numero == 0:
        sys.exit()
    separador = ""
    for x in range(1, numero+1):
        if x*x <= (numero):
            print("%s%d" % (separador, x*x), end="")
            separador = " "
        else:
            break

    print("")
