def solution(line):
    answer = []
    s = set()
    start = True
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    
    for i, l in enumerate(line):
        A, B, E = l[0], l[1], l[2]
        
        for ii, ll in enumerate(line):
            
            if i == ii:
                continue
            
            C, D, F = ll[0], ll[1], ll[2]
            
            if A*D - B*C == 0:
                continue            
            
            x = (B*F - E*D) / (A*D - B*C)
            y = (E*C - A*F) / (A*D - B*C)
            
            if x%1 != 0 or y%1 != 0:
                continue
            
            x, y = int(x), int(y)
            s.add((x, y))
            
            if start:
                min_x, max_x, min_y, max_y = x, x, y, y
                start = False
                continue
                
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
    
    zero_y, zero_x = 0, 0
    diff_x = max_x - min_x + 1
    
    if min_y < 0:
        zero_y = abs(min_y)
    else:
        zero_y = -1*min_y
        
    if min_x < 0:
        zero_x = abs(min_x)
    else:
        zero_x = -1*min_x
    
    for ss in s:
        x, y = ss
        x = x+zero_x
        y = y+zero_y
        
        while y > len(answer)-1:
            answer.append('.'*diff_x)
        
        st = answer[y]
        result = ''
        if x > 0:
            result += st[:x]
        result += '*'
        if x+1 < len(st):
            result += st[x+1:]
        answer[y] = result
    
    answer.reverse()
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges