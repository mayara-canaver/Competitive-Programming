from math import pow
import sys

valores = list(map(float, input().split()))
valores = sorted(valores, reverse=True)

a, b, c = valores

if a >= b+c:
    print("NAO FORMA TRIANGULO")
    sys.exit()
if pow(a, 2) == pow(b, 2) + pow(c, 2):
    print("TRIANGULO RETANGULO")
if pow(a, 2) > pow(b, 2) + pow(c, 2):
    print("TRIANGULO OBTUSANGULO")
if pow(a, 2) < pow(b, 2) + pow(c, 2):
    print("TRIANGULO ACUTANGULO")
if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or c == a:
    print("TRIANGULO ISOSCELES")