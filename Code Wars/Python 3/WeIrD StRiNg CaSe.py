def to_weird_case(string):
    
    string_final = ""
    rodada = 0
    
    for parte in range(len(string)):
        
        if " " in string[parte]:
            string_final += " "
            rodada = -1
        else:
            if rodada % 2 == 0:
                string_final += string[parte].upper()
            else:
                string_final += string[parte].lower()
        
        rodada += 1
        
    return string_final