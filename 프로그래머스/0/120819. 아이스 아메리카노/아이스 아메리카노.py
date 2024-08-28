def solution(money):
    mus = [] #[잔 수, 남는 돈] 

    cups, last_money = divmod(money, 5500)
    mus.append(cups)
    mus.append(last_money)
    return mus