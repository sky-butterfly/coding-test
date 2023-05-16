def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        text = str(i)
        text = text.replace('5', '')
        text = text.replace('0', '')
        
        if len(text) == 0:
            answer.append(i)
    
    
    if len(answer) == 0:
        answer = [-1]
    
    return answer
