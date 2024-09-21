from math import sqrt

def solution(n):
    answer = 0
    
    a, b = divmod(sqrt(n), 1)
    
    if b > 0 :
        answer = 2
    else:
        answer = 1
    
    return answer