soma = 0

while True:
    try:
        palavra = input()
        if palavra == "caw caw":
            print(soma)
            soma = 0
        else:
            palavra = palavra.replace("-", "0").replace("*", "1")
            palavra = int(palavra, 2)
            soma += palavra
    except EOFError:
        break
