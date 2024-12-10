repeticao = int(input())
x = 0

while x < repeticao:
    entradas = input().split()
    a, b = entradas
    if a == "tesoura":
        if b == "papel":
            print("Caso #%d: Bazinga!" % (x+1))
        elif b == "Spock":
            print("Caso #%d: Raj trapaceou!" % (x+1))
        elif b == "lagarto":
            print("Caso #%d: Bazinga!" % (x+1))
        elif b == "pedra":
            print("Caso #%d: Raj trapaceou!" % (x+1))
        else:
            print("Caso #%d: De novo!" % (x+1))
    elif a == "papel":
        if b == "pedra":
            print("Caso #%d: Bazinga!" % (x+1))
        elif b == "lagarto":
            print("Caso #%d: Raj trapaceou!" % (x+1))
        elif b == "Spock":
            print("Caso #%d: Bazinga!" % (x+1))
        elif b == "tesoura":
            print("Caso #%d: Raj trapaceou!" % (x+1))
        else:
            print("Caso #%d: De novo!" % (x+1))
    elif a == "pedra":
        if b == "lagarto":
            print("Caso #%d: Bazinga!" % (x+1))
        elif b == "Spock":
            print("Caso #%d: Raj trapaceou!" % (x+1))
        elif b == "papel":
            print("Caso #%d: Raj trapaceou!" % (x+1))
        elif b == "tesoura":
            print("Caso #%d: Bazinga!" % (x+1))
        else:
            print("Caso #%d: De novo!" % (x+1))
    elif a == "lagarto":
        if b == "Spock":
            print("Caso #%d: Bazinga!" % (x+1))
        elif b == "pedra":
            print("Caso #%d: Raj trapaceou!" % (x+1))
        elif b == "tesoura":
            print("Caso #%d: Raj trapaceou!" % (x+1))
        elif b == "papel":
            print("Caso #%d: Bazinga!" % (x+1))
        else:
            print("Caso #%d: De novo!" % (x+1))
    elif a == "Spock":
        if b == "tesoura":
            print("Caso #%d: Bazinga!" % (x+1))
        elif b == "lagarto":
            print("Caso #%d: Raj trapaceou!" % (x+1))
        elif b == "papel":
            print("Caso #%d: Raj trapaceou!" % (x+1))
        elif b == "pedra":
            print("Caso #%d: Bazinga!" % (x+1))
        else:
            print("Caso #%d: De novo!" % (x+1))
    x = x + 1
