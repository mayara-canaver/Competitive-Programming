while True:
    frase = input().upper().split()

    if frase[0][0] == "*":
        break

    count = 0

    letra = frase[0][0]

    for palavra in frase:

        if palavra[0] != letra:
            count += 1

    if count > 0:
        print("N")
    else:
        print("Y")