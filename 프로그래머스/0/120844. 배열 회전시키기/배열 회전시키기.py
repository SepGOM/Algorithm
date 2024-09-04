def solution(numbers, direction):
    answer = []
    
    for i in range(len(numbers)):
        if direction == "right":
            answer.append(numbers[(i - 1) % len(numbers)])
        else:
            answer.append(numbers[(i + 1) % len(numbers)])
    return answer