while True:
    soma = 0
    x = int(input())
    if x == 0:
        break
    if x % 2 == 0:
        for numero in range(5):
            soma += x
            x += 2
    else:
        x += 1
        for numero in range(5):
            soma += x
            x += 2
    print(soma)