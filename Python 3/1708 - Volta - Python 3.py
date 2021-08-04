while True:
    x1, x2_3 = input().split("+")
    x2, x3 = x2_3.split("=")
    x1, x2, x3 = x1[::-1], x2[::-1], x3[::-1]
    x1, x2, x3 = int(x1), int(x2), int(x3)

    if x1 + x2 == x3:
        print("True")
    else:
        print("False")

    if x1 == x2 == x3 == 0:
        break
