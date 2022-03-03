while True:
    try:

        soma, J = input().split("=")
        R, L = soma.split("+")

        if R.isalpha():
            print(int(J) - int(L))

        if L.isalpha():
            print(int(J) - int(R))

        if J.isalpha():
            print(int(R) + int(L))

    except EOFError:
        break
