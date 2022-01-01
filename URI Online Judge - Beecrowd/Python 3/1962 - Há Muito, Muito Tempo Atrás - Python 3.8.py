s, t, f = list(map(int, input().split()))

hora_final = t + f

final = s + hora_final

if final > 24:
    final = final - 24
    print(final)
elif final < 0:
    final = 24 + final
    print(final)
else:
    print(final)