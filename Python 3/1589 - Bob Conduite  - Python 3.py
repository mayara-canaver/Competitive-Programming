numeros = input().split()
numeros = list(map(float, numeros))
a, b = numeros
if a > 0 and b < 0:
    quociente = a/b
    b = b * (-1)
    resto = a%b
elif b > 0 and a < 0:
    b = b * (-1)
    a = a * (-1)
    quociente = round(a//b)
    resto = (a%b)*(-1)
elif a < 0 and b < 0:
    b = b * (-1)
    quociente = round(a//b)
    resto = ((b * quociente) - a)*(-1)
    quociente = quociente * (-1)
else:
    quociente = a/b
    resto = a%b

print("%d %d" % (quociente, resto))
