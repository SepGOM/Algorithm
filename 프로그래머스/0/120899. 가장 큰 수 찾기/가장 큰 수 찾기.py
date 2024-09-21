def solution(array):
    answer = []
    
    for index, num in enumerate(array):
        if max(array) == num:
            answer.append(num)
            answer.append(index)
    
    return answer