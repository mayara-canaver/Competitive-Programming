frango, bife, arroz = list(map(int, input().split()))
sem_frango, sem_bife, sem_arroz = list(map(int, input().split()))

t_frango = frango - sem_frango
t_bife = bife - sem_bife
t_arroz = arroz - sem_arroz

total = 0

if t_frango < 0:
    total += t_frango
if t_bife < 0:
    total += t_bife
if t_arroz < 0:
    total += t_arroz

print(abs(total))
