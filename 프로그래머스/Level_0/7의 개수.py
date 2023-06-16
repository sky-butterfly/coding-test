def solution(array):
    answer = 0
    
    for a in array:
        s = str(a)
        n = len(s) - len(s.replace('7', ''))
        answer += n
    
    return answer