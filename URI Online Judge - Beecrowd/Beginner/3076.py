from math import ceil

while True:
    try:
        ano = int(input())
        
        seculo = ceil(ano / 100)
            
        print(seculo)

    except EOFError:
        break
