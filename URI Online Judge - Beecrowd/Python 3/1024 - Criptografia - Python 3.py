vezes = int(input())

for x in range(vezes):
    palavra = input().split()
    palavra_inteira = palavra[0]
    parte_palavra = palavra[1]
    if palavra_inteira.endswith(parte_palavra):
        print("encaixa")
    else:
        print("nao encaixa")