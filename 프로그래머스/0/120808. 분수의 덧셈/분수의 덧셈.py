def lcm(a, b):  # 최소공배수
    i = 0
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
	        return i
        
def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    denom = lcm(denom1, denom2)
    numer = (numer1 * (denom / denom1)) + (numer2 * (denom / denom2))
    
    gcdA = gcd(denom, numer)
    
    denom_A, numer_A = denom / gcdA, numer / gcdA
    answer.append(numer_A)
    answer.append(denom_A)
    
    return answer