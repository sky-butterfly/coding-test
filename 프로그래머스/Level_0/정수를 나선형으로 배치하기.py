def solution(n):
    answer = []
    r = 'R'
    l = 'L'
    u = 'U'
    d = 'D'
    x = r
    
    for i in range(n):
        arr = []
        for k in range(n):
            arr.append(0)
        answer.append(arr)
    
    i = 0
    num = n
    count = 0
    line = 0
    while i < n*n: 
        if count == 2:
            count = 0
            num -= 1
        
        count += 1
        
        if x == r:
            line += 1
            for k in range(line-1, line+num-1):
                i += 1
                answer[line-1][k] = i
            x = d
            
            if num == n:
                count = 2
            continue
        if x == d:
            for k in range(line, line+num):
                i += 1
                answer[k][n-line] = i
            x = l
            continue
        if x == l:
            for k in range(n-line-1, line-2, -1):
                i += 1
                answer[n-line][k] = i
            x = u            
            continue
        if x == u:
            for k in range(n-line-1, line-1, -1):
                i += 1
                answer[k][line-1] = i
            x = r
            continue
    return answer