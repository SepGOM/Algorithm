def solution(emergency):
    answer = []
    
    for i in emergency:
        order = 1
        for j in emergency:
            if i < j:
                order += 1
        answer.append(order)
        
    return answer