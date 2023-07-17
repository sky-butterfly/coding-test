def solution(data, col, row_begin, row_end):
    answer = -1
    
    l = sorted(data, key=lambda x : (x[col-1], -x[0]))
    
    for i in range(row_begin-1, row_end):
        S_i = 0
        for j in l[i]:
            S_i += (j%(i+1))
                
        if answer == -1:
            answer = S_i
            continue
            
        answer ^= S_i
        
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges