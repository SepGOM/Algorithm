def solution(sides):
    
    if len(set(sides)) == 1:    #정삼각형
        return 1
    elif len(set(sides)) == 2 & sides.count(max(sides)) == 2:   #이등변삼각형
        return 1
    else:   #삼각형
        Max = max(sides)
        SideSum = 0
        
        for i in sides:
            if i != Max:
                SideSum += i
                
        if Max < SideSum:
            return 1
        else:
            return 2
 