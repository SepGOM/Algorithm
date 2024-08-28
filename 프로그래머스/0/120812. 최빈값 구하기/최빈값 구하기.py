def solution(array):
    array.sort()

    cntList = []
    maxCnt = 0
    ans = 0

    if len(array) == 1:
        ans = array[0]

    else:
        for i in set(array):
            if  maxCnt <= array.count(i):
                maxCnt = array.count(i)
                ans = i
                cntList.append(maxCnt)
                print(cntList)

            if cntList.count(max(cntList)) >= 2:
                ans = -1     
                
    return ans