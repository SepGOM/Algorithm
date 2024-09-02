def solution(hp):
    cnt = 0
    
    for i in [5, 3, 1]:
        dam, hp = divmod(hp, i)
        cnt += dam

    return cnt