numero = int(input())

ano = numero//365

mes = (numero - ano*365)//30

dia = ((numero - ano*365) - mes*30)

print("%d ano(s)\n%d mes(es)\n%d dia(s)" % (ano, mes, dia))

