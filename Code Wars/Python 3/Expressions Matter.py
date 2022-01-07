def expression_matter(a, b, c):
    jeito_1 = a * (b + c)
    
    jeito_2 = a * b * c
    
    jeito_3 = (a + b) * c
    
    jeito_4 = a + b * c
    
    jeito_5 = a + b + c
    
    resultados = [jeito_1, jeito_2, jeito_3, jeito_4, jeito_5]
    
    maior = max(resultados)
    
    return maior