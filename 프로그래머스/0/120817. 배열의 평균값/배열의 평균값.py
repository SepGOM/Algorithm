def solution(numbers):
    sum = 0
    i = 0
    
    for i in range(len(numbers)):
        sum += numbers[i]
        
    return sum / len(numbers)