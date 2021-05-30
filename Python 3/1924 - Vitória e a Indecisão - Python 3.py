numeros = list(map(int, input().split()))
maior = max(numeros)
numeros.remove(maior)
menor = min(numeros)

numeros.remove(menor)
soma = sum(numeros)

if soma > maior:
    print("S")
else:
    maiorzao = max(numeros)
    numeros.remove(maiorzao)
    nu = max(numeros)
    sominha = menor + nu
    if sominha > maiorzao:
        print("S")
    else:
        print("N")
