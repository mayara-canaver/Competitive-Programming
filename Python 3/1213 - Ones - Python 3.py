numero = input().split()
numero = list(map(float, numero))
a, b, c = numero
perimetro = a + b + c
trapezio = ((a+b)*c)/2
soma_ab, soma_ac, soma_bc = a+b, a+c, b+c
if a>=b and a>=c:
    if soma_bc>a:
        print("Perimetro = %.1f" % perimetro)
    else:
        print("Area = %.1f" % trapezio)
elif b>=a and b>=c:
    if soma_ac>b:
        print("Perimetro = %.1f" % perimetro)
    else:
        print("Area = %.1f" % trapezio)
elif c>=b and c>=a:
    if soma_ab>c:
        print("Perimetro = %.1f" % perimetro)
    else:
        print("Area = %.1f" % trapezio)