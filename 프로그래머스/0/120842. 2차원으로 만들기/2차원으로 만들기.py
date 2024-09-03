def solution(num_list, n):
    ans = []

    for i in range(0, len(num_list), n):
        ans.append(num_list[0 + i : n + i])
    
    return ans