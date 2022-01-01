def soma(i, count, sominha):
    sominha += i
    listinha.append(sominha)
    count += 1
    if count == i or sominha >= final:
        return sominha
    else:
        return soma(i, count, sominha)


while True:
    final, numero = list(map(int, input().split()))

    if final == numero == 0:
        break

    listinha = []

    resultado, sominha = 0, 0

    for j in range(numero):
        for i in range(j):
            count = 0
            resultado += soma(i + 1, count, sominha)
            listinha.append(resultado)

            print(resultado, final)

            if final in listinha:
                print("possivel")
                break
            else:
                print("impossivel")
                break


    resultado, sominha = 0, 0

    for j in range(numero, 0, -1):
        for i in range(j):
            count = 0
            resultado += soma(i + 1, count, sominha)
            listinha.append(resultado)

            print(resultado, final)

            if final in listinha:
                print("possivel")
                break
            else:
                print("impossivel")
                break

