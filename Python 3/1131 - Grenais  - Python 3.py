vezes = int(input())

total_carneiro, valor_carneiro, roubo, max_count, conta_par = 0, 0, 0, 0, 0
pegou_par = False
carneiros = list(map(int, input().split()))

soma_carneiro = sum(carneiros)
count = 0

while True:
    if count < 0 or count >= len(carneiros):
        break
    valor_carneiro = carneiros[count]
    if valor_carneiro != 0:
        roubo = roubo + 1
    carneiros[count] = valor_carneiro - 1
    if valor_carneiro % 2 == 0:
        count = count - 1
        pegou_par = True
    else:
        count = count + 1
        max_count = roubo

if pegou_par:
    max_count += 1

total_carneiro = soma_carneiro - roubo

print(max_count, total_carneiro)
