def solution(n, l, r):
    answer = 0
    obj = {}
    n_obj = {0:1}
    total = 20
            
    for i in range(1, 21):
        if i == 1:
            n_obj[i] = 4
            continue
        n_obj[i] = n_obj[i-1] * 4
    
    answer = dfs(l, r, n, n_obj, answer)
    
    return answer

def dfs(l, r, n, n_obj, answer):
    
    size = 5**(n-1)
    start, end = l // size, r // size
    l_add, r_add = l % size, r % size
    if l_add > 0:
        start += 1    
    if r_add > 0:
        end += 1
        
    for i in range(start, end+1):
            
        start_num = size * (i-1) + 1
        end_num = size * i
        if i == 3:
            l = end_num+1
            continue
        
        if l > start_num: 
            l = l%size
            if l == 0:
                l = size
                
            if r <= end_num:   
                r = r%size
                if r == 0:
                    r = size
                answer += dfs(l, r, n-1, n_obj, 0)
            else:
                end_num = end_num%size
                if end_num == 0:
                    end_num = size
                answer += dfs(l, end_num, n-1, n_obj, 0)
        else:
            l = l%size
            if l == 0:
                l = size
            if r >= end_num:
                answer += n_obj[n-1]
            else:
                r = r%size
                if r == 0:
                    r = size
                answer += dfs(l, r, n-1, n_obj, 0)
        l = end_num+1
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
    