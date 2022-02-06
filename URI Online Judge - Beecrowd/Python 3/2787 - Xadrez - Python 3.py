linha = int(input())
coluna = int(input())

if linha % 2 == 0 and coluna % 2 == 0:
    print(1)
elif linha % 2 == 0 and coluna % 2 != 0:
    print(0)
elif linha % 2 != 0 and coluna % 2 == 0:
    print(0)
else:
    print(1)
