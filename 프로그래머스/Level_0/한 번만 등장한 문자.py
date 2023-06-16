def solution(s):
    answer = []
    
    for ss in s:
        if len(s) - len(s.replace(ss, '')) == 1:
            answer.append(ss)
            
    answer.sort()
    
    return ''.join(answer)