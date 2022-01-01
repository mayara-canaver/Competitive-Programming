while True:
    try:
        vezes = int(input())

        numero = list(map(int, input().split()))

        qtd_1 = numero.count(1)
        qtd_0 = numero.count(0)

        if qtd_0 > qtd_1:
            print("Y")
        else:
            print("N")

    except EOFError:
        break
