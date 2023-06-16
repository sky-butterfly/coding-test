from itertools import combinations

def solution(dots):
    answer = 0
    combi = list(combinations(dots, 2))
    
    for k, c in enumerate(combi):
        for i in range(k, len(combi)):
            b = combi[i]
            if c[0] in b or c[1] in b:
                continue
            
            x1 = c[0][0]
            y1 = c[0][1]
            x2 = c[1][0]
            y2 = c[1][1]
            x3 = b[0][0]
            y3 = b[0][1]
            x4 = b[1][0]
            y4 = b[1][1]
            
            a = (y2-y1) / (x2-x1)
            b = (y4-y3) / (x4-x3)
            
            if a == b:
                answer =1
                break
        if answer == 1:
            break
    
    return answer