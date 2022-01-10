def duplicate_elements(m, n):
    confere = False
    
    for elemento in range(len(m)):
        if m[elemento] in n:
            confere = True
        
    return confere