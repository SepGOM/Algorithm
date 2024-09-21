def solution(n):
    temp = []
    answer = []
    
    i = 2
    
    while i <= n :
        if n % i == 0:
            temp.append(i)
            n = n // i
            
        else:
            i += 1
            
            
    for j in temp:
        if j not in answer:
            answer.append(j)
             
    return answer