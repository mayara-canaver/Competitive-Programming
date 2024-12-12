def quebra_chocolate(x):
    if x < 2:
        return 1
    else:
        x = x // 2

    return quebra_chocolate(x) * 4


lado = int(input())

print(quebra_chocolate(lado))
