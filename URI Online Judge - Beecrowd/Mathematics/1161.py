dias = 0
numero = int(input())

for x in range(numero):
  x = float(input())
  while x > 1:
      x = x/2
      dias = dias + 1
  print("%d dias" %dias)
  dias = 0
