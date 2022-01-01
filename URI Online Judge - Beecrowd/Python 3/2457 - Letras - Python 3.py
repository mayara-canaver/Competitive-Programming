from collections import Counter

vezes = int(input())

lista = list(map(int, input().split()))

print(max(Counter(lista).most_common(), key=lambda p: (p[1], p[0]))[0])
