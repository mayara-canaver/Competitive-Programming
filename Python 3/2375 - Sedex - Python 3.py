n, c = list(map(int, input().split()))

total = 0
confirma = False

for x in range(n):
    s, e = list(map(int, input().split()))
    total -= s
    total += e
    if total > c:
        confirma = True

if confirma:
    print("S")
else:
    print("N")
