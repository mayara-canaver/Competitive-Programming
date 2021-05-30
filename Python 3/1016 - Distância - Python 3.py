numero = int(input())

for figurinha in range(numero):
    figurinha = input().split()
    figurinha = list(map(int, figurinha))
    while figurinha[1] != 0:
        resto = figurinha[0] % figurinha[1]
        figurinha[0] = figurinha[1]
        figurinha[1] = resto

    print(figurinha[0])
    figurinha = 0

