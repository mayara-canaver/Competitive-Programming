dia_inicio = input().split()
dia_inicio = int(dia_inicio[1])

hora_inicio = input().split()
hora_inicial, minuto_inicial, segundo_inicial = int(hora_inicio[0]), int(hora_inicio[2]), int(hora_inicio[4])

dia_final = input().split()
dia_final = int(dia_final[1])

hora_finalzinho = input().split()
hora_final, minuto_final, segundo_final = int(hora_finalzinho[0]), int(hora_finalzinho[2]), int(hora_finalzinho[4])

soma_final = segundo_final + minuto_final*60 + hora_final*3600 + dia_final*86400
soma_inicial = segundo_inicial + minuto_inicial*60 + hora_inicial*3600 + dia_inicio*86400

soma_total = soma_final - soma_inicial

dia_total, hora_total, minuto_total, segundo_total = 0, 0, 0, 0

setMinutesSeconds = 60
setHourSeconds= setMinutesSeconds * 60
setDaySeconds = setHourSeconds * 24

dia_total = int(soma_total/setDaySeconds)
soma_total = soma_total%setDaySeconds
hora_total = int(soma_total/setHourSeconds)
soma_total = soma_total%setHourSeconds
minuto_total = int(soma_total/setMinutesSeconds)
soma_total = soma_total%setMinutesSeconds

print("%d dia(s)" % dia_total)
print("%d hora(s)" % hora_total)
print("%d minuto(s)" % minuto_total)
print("%d segundo(s)" % soma_total)
