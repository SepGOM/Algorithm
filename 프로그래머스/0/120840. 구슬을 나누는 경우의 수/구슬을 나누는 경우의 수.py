def solution(balls, share):
    import math
    return math.factorial(balls) // (math.factorial(balls - share) * math.factorial(share))