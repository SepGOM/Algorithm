def solution(my_string):
    rev_str = ''
    
    for i in my_string:
        rev_str = i + rev_str
        
    return rev_str