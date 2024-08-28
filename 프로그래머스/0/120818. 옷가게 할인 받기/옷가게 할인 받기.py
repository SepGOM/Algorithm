def solution(price):
    retPri = price
    
    if 100000 <= price < 300000:
        retPri = price - (price * 0.05)
    elif 300000 <= price < 500000:
        retPri = price - (price * 0.10)
    elif 500000 <= price:
        retPri = price - (price * 0.20)
    
    return int(retPri)