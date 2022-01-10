def well(x):
    quantidade = x.count("good")
    
    if quantidade == 0:
        return "Fail!"
    elif quantidade < 3:
        return "Publish!"
    else:
         return "I smell a series!"