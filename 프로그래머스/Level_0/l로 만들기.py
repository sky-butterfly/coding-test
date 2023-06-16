def solution(myString):
    answer = ''
    
    for m in myString:
        if ord(m) < ord('l'):
            answer += 'l'
            continue
        answer += m
    
    return answer