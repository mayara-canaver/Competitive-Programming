numero = int(input())

minutos, segundos, horas = 0, 0, 0
minutos = numero//60
segundos = numero%60

if minutos > 59:
    horas = minutos//60
    minutos = minutos - horas*60

print("%d:%d:%d" % (horas, minutos, segundos))

