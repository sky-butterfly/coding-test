def solution(picture, k):
    answer = []
    
    for p in picture:
        s = ''
        for pp in p:
            for i in range(k):
                s += pp
        
        for i in range(k):
            answer.append(s)
    
    return answer