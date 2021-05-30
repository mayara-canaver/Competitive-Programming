import sys
import math

while True:
  try:
    linha = input().split()
    linha = list(map(int, linha))
    total = math.factorial(linha[0]) + math.factorial(linha[1])
    print(total)
    linha = 0
  except EOFError:
      break