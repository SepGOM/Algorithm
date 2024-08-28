def solution(array, height):
    tall_hi = []
    array.sort()
    
    for i in range(len(array)):
        if array[i] > height:
            tall_hi.append(array[i])
    return len(tall_hi)