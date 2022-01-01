from math import sqrt

while True:
    try:
        degraus = int(input())
        altura, comprimento, largura = list(map(int, input().split()))

        altura /= 100
        comprimento /= 100
        largura /= 100

        diagonal = sqrt(comprimento ** 2 + altura ** 2)

        total = ((diagonal * largura) * degraus)

        print("%.4f" % total)

    except EOFError:
        break
