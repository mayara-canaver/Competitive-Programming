vezes = int(input())

for x in range(vezes):
    n, m = list(map(int, input().split()))

    resultado = len(str(n ** m))

    print(resultado)
