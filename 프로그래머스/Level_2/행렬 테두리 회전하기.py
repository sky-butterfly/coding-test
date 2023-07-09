def solution(rows, columns, queries):
    answer = []
    
    arr = []
    
    for i in range(rows):
        a = []
        
        for j in range(1, columns+1):
            a.append((i*columns)+j)
            
        arr.append(a)
    
    for q in queries:
        mn = arr[q[0]-1][q[1]-1]
        a = []
        
        r_size = q[2] - q[0]
        c_size = q[3] - q[1]
        
        r = q[0]-1
        for i in range(c_size+1):
            c = q[1]-1+i
            a.append(arr[r][c])
            if len(a) > 1:
                aa = a.pop(0)
                arr[r][c] = aa
                if aa < mn:
                    mn = aa
                
        for i in range(1, r_size+1):
            r = q[0]-1+i
            a.append(arr[r][c])
            aa = a.pop(0)
            arr[r][c] = aa
            if aa < mn:
                mn = aa
                
        for i in range(1, c_size+1):
            c = q[3]-1-i
            a.append(arr[r][c])
            aa = a.pop(0)
            arr[r][c] = aa
            if aa < mn:
                mn = aa
        
        for i in range(1, r_size+1):
            r = q[2]-1-i
            a.append(arr[r][c])
            aa = a.pop(0)
            arr[r][c] = aa
            if aa < mn:
                mn = aa
        
        answer.append(mn)
        
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges