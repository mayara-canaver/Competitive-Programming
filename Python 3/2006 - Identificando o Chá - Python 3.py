numero = int(input())
resposta = list(map(int, input().split()))
count = 0

for x in resposta:
    if x == numero:
        count += 1
        
print(count)
