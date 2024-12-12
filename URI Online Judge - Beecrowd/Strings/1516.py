numeros = input().split()
numeros = list(map(float, numeros))
n, x, y = numeros

icm = n/(x+y)

print("%.2f" % icm)