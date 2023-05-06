def solution(arr):
    answer = []
    
    for a in arr :
        if a >= 50 and a%2 == 0:
            answer.append(int(a/2))
            continue
        if a < 50 and a%2 != 0:
            answer.append(a*2)
            continue
        answer.append(a)
    
    return answer