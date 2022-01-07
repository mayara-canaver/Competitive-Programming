def elevator(left, right, call):
    if left == call == right:
        return "right"
    elif (left == call) or (abs(left - call) < abs(right - call)):
        return "left"
    elif right == call or (abs(right - call) < abs(left - call)):
        return "right"
    else:
        return "right"