def solution(my_string):
    
    for i in 'abcdefghijklmnopqrstuvwxyz':
        my_string = my_string.replace(i, '')        
    
    return list(sorted(map(int,str(my_string))))