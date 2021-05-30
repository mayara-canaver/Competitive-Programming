import sys

while True:
    try:
        lesma = int(input())
        lesminhas = input().split()
        lesminhas = list(map(int, lesminhas))
        maior = max(lesminhas)
        if maior < 10:
            print(1)
        elif 10 <= maior < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        sys.exit()