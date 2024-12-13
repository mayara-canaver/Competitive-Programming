while True:
    valor_prod, valor_cliente = list(map(int, input().split()))
    
    if valor_prod == valor_cliente == 0:
        break
    
    troco = valor_cliente - valor_prod
    retorno = False
    
    lst_nota = [2, 5, 10, 20, 50, 100]
    
    for nota1 in lst_nota:
        for nota2 in lst_nota:
            if nota1 + nota2 == troco:
                retorno = True
    
    if retorno:
        print("possible")
    else:
        print("impossible")
