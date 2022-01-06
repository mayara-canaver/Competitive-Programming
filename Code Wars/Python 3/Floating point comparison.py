def approx_equals(a, b):
    
    if abs(a - b) <= 0.001 or abs(b - a)  <= -0.001:
        return True
    else:
        return False