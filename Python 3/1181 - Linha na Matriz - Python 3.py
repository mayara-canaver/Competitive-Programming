vezes = int(input())

for x in range(vezes):
    palavra = input()

    if len(palavra) > 3:
        print(3)
    else:
        one = 0
        two = 0

        if palavra[0] == "o":
            one += 1
        if palavra[1] == "n":
            one += 1
        if palavra[2] == "e":
            one += 1

        if palavra[0] == "t":
            two += 1
        if palavra[1] == "w":
            two += 1
        if palavra[2] == "o":
            two += 1

        if two > 1:
            print(2)

        if one > 1:
            print(1)
