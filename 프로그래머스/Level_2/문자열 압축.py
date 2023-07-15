from collections import defaultdict

def solution(s):
    answer = len(s)
    
    for i in range(len(s), 0, -1):
        
        a = 0
        
        n = len(s)//i
        
        pre = s[:i]
        cnt = 0
        j = 0
        a = 0
        while j < (n*i)+1:
            
            ss = s[j:j+i]
            
            if pre != ss:
                a += len(pre)
                if cnt > 1:
                    a += len(str(cnt))
                
                pre = ss
                cnt = 1
            else:
                cnt += 1
            
            if cnt > answer:
                cnt = -1
                break
            
            j+= i
        
        if cnt == -1:
            continue
        
        if cnt > 1:
            a += len(str(cnt))
        a += len(pre)
        
        if a < answer:
            answer = a
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges