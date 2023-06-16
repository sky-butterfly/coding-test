def solution(order):
    answer = 0
    latte = 'cafelatte'
    
    for o in order:
        if latte in o:
            answer += 5000
            continue
        answer += 4500
    
    return answer