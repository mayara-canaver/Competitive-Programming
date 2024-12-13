qtd_nomes = int(input())

lst_nome, lst_comp = [], []

for valor in range(qtd_nomes):
    comp, nome = list(input().split())

    lst_nome.append(nome)
    lst_comp.append(comp)

lst_nome.sort()

print("\n".join(lst_nome))

print("Se comportaram: %d | Nao se comportaram: %d" % (lst_comp.count("+"), lst_comp.count("-")))
