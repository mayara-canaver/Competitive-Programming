from collections import Counter
vezes = int(input())

for x in range(vezes):
    cheater = False
    total, almoco, janta = list(input()), list(input()), list(input())
    for letra in almoco:
        if letra in total:
            pass
        else:
            cheater = True
    for letra in janta:
        if letra in total:
            pass
        else:
            cheater = True
    total = list((Counter(total) - Counter(janta) - Counter(almoco)).elements())
    if len(total) > 0 and cheater is False:
        total = sorted(total)
        print("".join(total))
    elif cheater:
        print("CHEATER")
    else:
        print()