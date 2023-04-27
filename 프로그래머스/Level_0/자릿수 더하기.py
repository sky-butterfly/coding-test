def solution(n):
    answer = 0
    toStr = str(n)
    
    for s in toStr:
        answer += int(s)
    
    return answer