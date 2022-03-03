from sys import stdin

instancia = 1

while True:
    autor = stdin.readline().strip()

    if autor == "0":
        break
    else:
        if instancia > 1:
            print()
            
        print("Instancia %d" % instancia)

        entrada = input()

        if autor in entrada:
            print("verdadeira")
        else:
            print("falsa")

        instancia += 1