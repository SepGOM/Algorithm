def solution(rsp):
    ans = ''
    
    for i in range(1, len(rsp) + 1):
        if rsp[i - 1] == '2':
            ans += "0"
        elif rsp[i - 1] == '0':
            ans += "5"
        elif rsp[i - 1] == '5':
            ans += "2"

    return ans