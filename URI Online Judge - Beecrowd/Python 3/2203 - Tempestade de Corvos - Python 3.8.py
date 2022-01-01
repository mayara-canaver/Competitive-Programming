from math import sqrt

while True:
    try:

        xf, yf, xi, yi, vi, r1, r2 = list(map(float, input().split()))

        distancia = sqrt(pow((xi - xf), 2) + pow((yi - yf), 2))

        if (distancia + (1.5 * vi)) > (r1 + r2):
            print("N")
        else:
            print("Y")

    except EOFError:
        break
