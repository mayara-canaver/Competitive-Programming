while True:
    vezes = int(input())

    if vezes == 0:
        break

    for x in range(vezes):
        a, b, c, d, e = list(map(int, input().split()))

        if a <= 127 and (b >= 127 and c >= 127 and d >= 127 and e >= 127):
            print("A")
        elif b <= 127 and (a >= 127 and c >= 127 and d >= 127 and e >= 127):
            print("B")
        elif c <= 127 and (b >= 127 and a >= 127 and d >= 127 and e >= 127):
            print("C")
        elif d <= 127 and (b >= 127 and c >= 127 and a >= 127 and e >= 127):
            print("D")
        elif e <= 127 and (b >= 127 and c >= 127 and d >= 127 and a >= 127):
            print("E")
        else:
            print("*")
