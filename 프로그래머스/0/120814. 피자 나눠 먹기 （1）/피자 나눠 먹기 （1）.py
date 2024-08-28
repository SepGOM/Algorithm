def solution(n):  
    ans, b = divmod(n, 7)
    if b > 0:
        ans += 1
    return ans