def solution(my_string):
    
    for i in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz':
        my_string = my_string.replace(i, '')  
    
    answer = sum(list(map(int, str(my_string))))
    
    return answer