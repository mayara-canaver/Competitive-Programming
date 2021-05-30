
# numero final = impar -> 1 vence
# numero final = par -> 2 vence



m = 1
la = []
la.append(1)
while len(la) < 10000:
    lb = []
    for i in la:
        lb.append(m * i)
    la += lb
    m = -m


vezes = int(input())

G = [("Sanches", "Rusa"), ("Rusa", "Sanches")]
g = 0
for i in range(vezes):
    r = 0
    n, q = list(map(int, input().split()))
    lista = list(map(int, input().split()))
    # a, b = list(map(int, input().split()))
    r = sum(la[i] * lista[i] for i in range(n))
    w = G[g%2][r%2]
    print("%d %s" % (r, w))
    for j in range(q):
        x, y = map(int, input().split())
        r = r - la[x - 1] * lista[x - 1] + la[x - 1] * y
        r_mod = r % 2 if r > 0 else (-r) % 2
        lista[x-1] = y
        w = G[g % 2][r_mod]
        print("%d %s" % (r, w))
    g += 1



# for x in range(vezes):
#     mult = 0
#     lista1, lista2 = [], []
#
#     # o número de inteiros na sequência inicial e o número de substituições
#     n, q = list(map(int, input().split()))
#
#     lista_backup = list(map(int, input().split()))
#
#     if q % 2 == 0:
#         jogador1 = "Rusa"
#         jogador2 = "Sanches"
#     else:
#         jogador1 = "Sanches"
#         jogador2 = "Rusa"
#
#     lista = lista_backup
#
#     while len(lista) > 1:
#         lista1 = lista[::2]
#         lista2 = lista[1::2]
#         lista = []
#
#         if n % 2 != 0:
#             lista2.append(0)
#
#         # se nao tem trocas
#         print("cheguei no if de sem troca")
#         if q == 0:
#             for ele in range(len(lista1)):
#                 total = lista1[ele] + lista2[ele] * mult
#                 lista.append(total)
#
#         # se tem trocas
#         else:
#             print("cheguei no if de com troca")
#             # elemento SA da sequência inicial é substituído por B (SA = B)
#             a, b = list(map(int, input().split()))
#             lista1[a-1] = b
#             lista2[a-1] = b
#
#             for ele in range(len(lista1)):
#                 total = lista1[ele] + lista2[ele] * mult
#                 lista.append(total)
#
#         mult = - mult
#
#         print("cheguei aqui ha")
#         if lista[0] % 2 == 0:
#             print("%d %s" % (lista[0], jogador1))
#         else:
#             print("%d %s" % (lista[0], jogador2))
