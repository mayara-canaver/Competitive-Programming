entradas = input().split()
entradas = list(map(int, entradas))

a, b, c = entradas

a_b = b-a
b_c = c-b

if a_b < 0:
    a_b = a_b*(-1)

if b_c < 0:
    b_c = b_c * (-1)

if a < b:
    if b < c:
        if a_b > b_c:
            print(":(")
        else:
            print(":)")
    else:
        print(":(")
else:
    if c > b:
        print(":)")
    else:
        if a_b > b_c:
            print(":)")
        else:
            print(":(")
