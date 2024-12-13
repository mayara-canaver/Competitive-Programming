n, c, m = list(map(int, input().split()))

fig_carimbada = list(map(int, input().split()))

fig_comprada = list(map(int, input().split()))

tamanho = len(fig_carimbada)

total = 0

for figurinha in fig_comprada:
    if figurinha in fig_carimbada:
        total += 1
        fig_carimbada.remove(figurinha)

print(tamanho - total)
