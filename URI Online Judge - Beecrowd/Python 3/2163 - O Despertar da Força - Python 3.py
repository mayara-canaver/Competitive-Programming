linha, coluna = list(map(int, input().split()))

matriz = []

for inner_linha in range(linha):
    lst_numeros = []
    lst_coluna = list(map(int, input().split()))

    matriz.append(lst_coluna)

valor_x_final, valor_y_final = 0, 0

for x in range(1, linha - 1):
    for y in range(1, coluna - 1):
        if matriz[x][y] == 42:
            if matriz[x - 1][y - 1] == 7 and matriz[x - 1][y] == 7 and matriz[x - 1][y + 1] == 7 and matriz[x][y - 1] == 7 and matriz[x][y + 1] \
                == 7 and matriz[x + 1][y - 1] == 7 and matriz[x + 1][y] == 7 and matriz[x + 1][y + 1] == 7:
                    valor_x_final, valor_y_final = x + 1, y + 1
                    break

print(valor_x_final, valor_y_final)
