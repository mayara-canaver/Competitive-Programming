valor = input().split(" ")
valor = list(map(int, valor))

maior_ab = (valor[0]+valor[1]+abs(valor[0]-valor[1]))/2

maior_ac = (maior_ab+valor[2]+abs(maior_ab-valor[2]))/2

print("%d eh o maior" %maior_ac)