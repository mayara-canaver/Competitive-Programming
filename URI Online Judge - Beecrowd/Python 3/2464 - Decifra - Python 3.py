comprimento, quantidade = list(map(int, input().split()))

resultado = ((comprimento - (quantidade - 1)) ** 2) + quantidade - 1

print(resultado)
