def solution(hp):
    answer = 0
    
    if hp == 0 :
        return answer
    
    x = int(hp/5)
    answer += x
    hp -= (x * 5)
    
    if hp < 1:
        return answer
    
    x = int(hp/3)
    answer += x
    hp -= (x * 3)
    if hp < 1:
        return answer
    
    answer += hp
    
    return answer