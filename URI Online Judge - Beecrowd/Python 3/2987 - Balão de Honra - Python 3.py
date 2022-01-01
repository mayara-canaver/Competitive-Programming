tabela = {"1": 2, "2": 5, "3": 5, "4": 4, "5": 5,
          "6": 6, "7": 3, "8": 7, "9": 6, "0": 6}
soma = 0
numero = int(input())
for x in range(numero):
     valor = input()
     for y in valor:
         if y in tabela:
             soma = soma + tabela[y]
         else:
             pass
     print("%d leds" %soma)
     soma = 0


