def solution(slice, n):
    ans, b = divmod(n, slice)
    if b > 0: 
        ans += 1
    return ans