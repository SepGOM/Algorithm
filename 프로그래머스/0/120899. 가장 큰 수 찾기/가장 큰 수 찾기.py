def solution(array):
    
    for index, num in enumerate(array):
        if max(array) == num:
            return [num, index]