import sys

while True:
    try:
        inst = input().split()
        inst = list(map(int, inst))
        r1, x1, y1, r2, x2, y2 = inst
        raiox1 = r1 - x1
        raiox12 = r1 + x1
        raioy1 = r1 - y1
        raioy12 = r1 + y1
        if r2 > r1 :
            print("MORTO")
        elif r1 == r2 and x1 == x2 and y1 == y2:
            print("RICO")
        elif r1 == r2 and x1 < x2 and y1 == y2:
            print("RICO")
        elif (raiox1 <= x2 <= raiox12) and (raioy1 <= y2 <= raioy12):
            print("RICO")
        else:
            print("MORTO")

    except EOFError:
        sys.exit()