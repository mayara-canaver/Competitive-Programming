a, b, c = int(input()), int(input()), int(input())

if a + b < c:
    maior = c
    print(a*4 + b* 2)
elif a + c < b:
    maior = b
    print(a*2 + c* 2)
elif c + b < a:
    maior = a
    print(c*4 + b* 2)
else:
    print(a * 2 + c * 2)