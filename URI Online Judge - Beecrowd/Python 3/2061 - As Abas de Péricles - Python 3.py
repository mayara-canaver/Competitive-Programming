import re
vezes = 0

while True:
    try:
        vezes += 1
        substring = input()
        string = input()
        count = 0

        for match in re.finditer(substring, string):
            count += 1
            s = match.start()
            e = match.end()

        s += 1

        print("Caso #%d:" % vezes)

        if count == 0:
            print("Nao existe subsequencia")
        else:
            print("Qtd.Subsequencias: %d" % count)
            print("Pos: %d" % s)

        print()

    except EOFError:
        break
