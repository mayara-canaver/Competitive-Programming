from math import floor

def solution(year):
    if year % 100 == 0:
        return floor(year / 100)
    else:
        return floor((year / 100) + 1)
