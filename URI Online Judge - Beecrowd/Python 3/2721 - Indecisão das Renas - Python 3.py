lst_rena = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]

numero = sum(list(map(int, input().split())))

numero %= 9

if numero == 0:
    print(lst_rena[-1])
else:
    print(lst_rena[numero - 1])

