x = int(input())
y = int(input())

soma = 0

if x < y:
    for numero in range(x, y+1):
        if numero%13 == 0:
            pass
        else:
            soma += numero

if y < x:
    for numero in range(y, x):
        if numero % 13 == 0:
            pass
        else:
            soma += numero

print(soma)