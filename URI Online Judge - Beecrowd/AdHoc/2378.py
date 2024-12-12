estrada, pedagio = list(map(int, input().split()))

qtd_pedagio = estrada // pedagio

custo, valor_pedagio = list(map(int, input().split()))

custo_km = estrada * custo

total_pedagio = (qtd_pedagio * valor_pedagio) + custo_km

print(total_pedagio)
