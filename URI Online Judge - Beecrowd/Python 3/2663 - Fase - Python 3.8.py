vezes = int(input())
total = ord("z") - ord("a")

for x in range(vezes):
    letra1, letra2 = list(input().split())
    soma = 0

    for c in range(len(letra1)):
        if ord(letra1[c]) <= ord(letra2[c]):
            soma += abs(ord(letra2[c]) - ord(letra1[c]))
        else:
            soma += ord(letra2[c]) - ord(letra1[c]) + 26

    print(soma)
