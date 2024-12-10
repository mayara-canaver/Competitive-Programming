tempo = list(map(int, input().split()))
hi, mi, hf, mf = tempo

hi *= 60
hf *= 60

inicio, final, hora_total, minuto_total = 0, 0, 0, 0

inicio = hi + mi
final = hf + mf

if inicio >= final:
    hora_total = final - inicio + 24 * 60
    minuto_total = hora_total % 60
    hora_total = hora_total // 60
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hora_total, minuto_total))

elif inicio < final:
    hora_total = final - inicio
    minuto_total = hora_total % 60
    hora_total = hora_total // 60
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hora_total, minuto_total))

