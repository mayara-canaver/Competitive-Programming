def fold_to(distance):
    
    dobras = 0
    resultado = 0.0001
    
    if distance < 0:
        return None
    else:
        while resultado < distance:
            dobras += 1
            
            resultado *= 2
        
        return dobras
    