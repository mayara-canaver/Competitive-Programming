def count_sheep(n):
    if n == 0:
        return ""
    else:
        frase = ""
        for n in range(1, n + 1):
            frase += (str(n) + " sheep...")
            
        return frase