def solution(array, n):
    cnt = 0
    for i in range(len(array)):
        if array[i - 1] == n:
            cnt += 1
    return cnt