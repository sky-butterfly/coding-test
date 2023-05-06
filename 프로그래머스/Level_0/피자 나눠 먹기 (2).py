def solution(n):
    answer = n * 6
    
    for i in range(max(n, 6), answer+1) :
        if (i%n == 0) and (i%6 == 0):
            return i // 6
    
    return answer