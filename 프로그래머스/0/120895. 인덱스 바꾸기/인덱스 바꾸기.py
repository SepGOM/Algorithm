def solution(my_string, num1, num2):
    string = list(map(str, my_string))   
    string[num1], string[num2] = string[num2], string[num1]
    return ''.join(string) 