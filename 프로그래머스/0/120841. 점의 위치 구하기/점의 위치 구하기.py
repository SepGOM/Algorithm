def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            ans = 1
        else: 
            ans = 4
    else:
        if dot[1] > 0:
            ans = 2
        else:
            ans = 3
    return ans