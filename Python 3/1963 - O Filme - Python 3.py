from math import sqrt
from math import floor
while True:
    numeros = list(map(int, input().split()))
    if len(numeros) == 1:
        break
    a, b, c = numeros
    total = floor(sqrt(a*b*(100/c)))
    print(total)

