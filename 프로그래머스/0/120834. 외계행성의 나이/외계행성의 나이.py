def solution(age):
    
    age_eng = ''
    eng = 'abcdefghij'
    
    for i in list(map(int, str(age))):
        age_eng = age_eng + eng[i]
        
    return age_eng