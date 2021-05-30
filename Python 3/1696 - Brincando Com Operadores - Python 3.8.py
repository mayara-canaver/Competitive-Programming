vezes = int(input())

for x in range(vezes):
    caracter = list(input().split())
    print(" ".join(sorted(caracter, key=lambda s: -len(s))))
