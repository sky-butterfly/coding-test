def solution(rsp):
    answer = ''
    
    for r in rsp :
        if r == '2' :
            answer += '0'
            continue
        elif r == '0' :
            answer += '5'
            continue
        answer += '2'
    
    return answer