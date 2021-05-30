numero = 0

def f(n):
    n = '%.1f'%n
    if n.endswith('.0'):
        n = n[:-2]
    return n

for x in range(0, 22, 2):
    x = x/10
    for y in range(1, 4):
        y = y + numero
        f(y)
        print("I=%s J=%s" % (f(x), f(y)))
    numero = numero + 0.2