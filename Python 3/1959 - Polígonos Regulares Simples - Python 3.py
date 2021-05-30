produtos = {"1001": 1.50, "1002": 2.50, "1003": 3.50, "1004": 4.50, "1005": 5.50}
valor, total = 0, 0
vezes = int(input())

for x in range(vezes):
    indice, quantidade = input().split()
    quantidade = int(quantidade)
    valor = produtos.get(indice)
    total += (valor * quantidade)

print("%.2f" % total)
