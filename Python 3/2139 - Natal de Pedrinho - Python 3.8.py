while True:
    numero, contrato = input().split()

    if numero == "0" and contrato == "0":
        break

    contrato = contrato.replace(numero, "")

    if contrato == "":
        contrato = "0"

    print(int(contrato))
