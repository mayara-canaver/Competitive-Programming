vezes = int(input())

for x in range(vezes):
    pessoa = input().split()
    p1, p2 = pessoa
    if p1 == "Thor":
        print("Y")
    else:
        print("N")