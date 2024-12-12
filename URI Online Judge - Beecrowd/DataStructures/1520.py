while True:
    try:
        qtd_caixas = int(input())

        lst_parafuso = []

        for linha in range(qtd_caixas):
            x, y = list(map(int, input().split()))
            lst_parafuso.extend(list(range(x, y + 1)))

        lst_parafuso.sort()

        lst_achados = []

        achar = int(input())

        for numero in range(len(lst_parafuso)):
            if lst_parafuso[numero] > achar:
                break
            if lst_parafuso[numero] == achar:
                lst_achados.append(numero)

        if len(lst_achados) > 0:
            print("%d found from %d to %d" % (achar, lst_achados[0], lst_achados[-1]))
        else:
            print("%d not found" % achar)

    except EOFError:
        break

    except ValueError:
        continue
