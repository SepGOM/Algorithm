def solution(n):
    ans, b = divmod(n, 6)
    if b > 0:
        for i in range(max(n, 6), (n * 6) + 1):
            if i % n == 0 and i % 6 == 0:
                ans = i // 6
                break
    return ans