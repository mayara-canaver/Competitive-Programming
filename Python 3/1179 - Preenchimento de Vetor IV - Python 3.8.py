while True:
    tamanho = int(input())
    t_l, t_c = 0, 0

    if tamanho == 0:
        break

    for linha in range(tamanho):
        # numero, a = 2, 1

        for coluna in range(tamanho):
            if linha + 1 > tamanho // 2:
                t_l = tamanho - linha -1
            else:
                t_l = linha
            if coluna + 1 > tamanho // 2:
                t_c = tamanho - coluna -1
            else:
                t_c = coluna
            if coluna < tamanho - 1:
                print('%3d ' % min(t_l+1,t_c+1), end='')
            else:
                print('%3d' % min(t_l+1,t_c+1), end='')
        print()

    print()