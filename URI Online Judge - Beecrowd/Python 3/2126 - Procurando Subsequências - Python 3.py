import re
from math import ceil

while True:
    try:
        string = input()

        string = re.split('(W)', string)

        vezes = int(input())
        count = 0

        for caracter in string:
            if caracter == "R":
                count += 1

            elif caracter == "W":
                count += 1

            elif len(caracter) >= 1:
                tamanho = len(caracter)
                count += ceil(tamanho / vezes)

        print(count)

    except EOFError:
        break
