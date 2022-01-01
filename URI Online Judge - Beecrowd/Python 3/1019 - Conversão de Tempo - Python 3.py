import statistics

numero = int(input())

for x in range(1, numero+1):
    idades = input().split()
    idades = list(map(int, idades))
    mediana = statistics.median(idades[1:])
    print("Case %d: %d" % (x, mediana))