def solution(n):
    answer = 0
    
    if n ** 0.5 == int(n ** 0.5):
        return 1
    else:
        return 2