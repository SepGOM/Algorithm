def solution(array, n):
    minus = []
    array.sort()
    
    for i in array:
        minus.append(abs(n - i))
    
    return array[minus.index(min(minus))]