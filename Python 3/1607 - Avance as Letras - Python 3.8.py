while True:
    num1, num2 = list(map(int, input().split()))

    if num1 == 0 and num2 == 0:
        break

    resultado = num1 + num2

    resultado = str(resultado)

    resultado = resultado.replace("0", "")

    resultado = int(resultado)

    print(resultado)
