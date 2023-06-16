def solution(strArr):
    answer = []
    
    for s in strArr:
        if ('ad' in s) == False:
            answer.append(s)
    
    return answer