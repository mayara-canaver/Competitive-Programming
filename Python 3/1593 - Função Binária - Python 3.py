def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


while True:
    try:
        vezes = int(input())
        for x in range(vezes):
            numero = int(input())
            numero = bin(numero)
            numero = str(numero)
            contar_1 = numero.count("1")
            print(contar_1)
    except EOFError:
        break


num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))