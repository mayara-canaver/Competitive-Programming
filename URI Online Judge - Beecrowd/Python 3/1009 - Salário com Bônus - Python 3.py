x = input().split()
y = input().split()

results1 = list(map(float, x))
results2 = list(map(float, y))

total = (results1[1]*results1[2])+(results2[1]*results2[2])

print("VALOR A PAGAR: R$ %0.2f" %total)