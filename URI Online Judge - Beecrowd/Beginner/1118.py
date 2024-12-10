vezes = int(input())

count = 0

for x in range(vezes):
    numero = int(input())
    if numero != 1:
        count += 1

print(count)
