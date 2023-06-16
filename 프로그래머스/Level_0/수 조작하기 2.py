def solution(numLog):
    answer = ''
    
    before = numLog[0]
    for n in numLog:
        if (n - before) == 1:
            answer += 'w'
        elif (before - n ) == 1:
            answer += 's'
        elif n - before == 10:
            answer += 'd'
        elif before - n == 10:
            answer += 'a'
        
        before = n
        continue
    
    return answer
