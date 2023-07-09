def solution(msg):
    answer = []
    cnt = ord('A')-ord('A')+1
    obj = {'A':cnt}
    
    for i in range(ord('B'), ord('Z')+1):
        cnt += 1
        obj[chr(i)] = cnt
    
    s = ''
    i = 0
    while i < len(msg):
        
        m = msg[i]
        if s+m in obj.keys():
            
            if i == (len(msg)-1):
                answer.append(obj[s+m])
                break
            
            s += m
            i += 1
            continue
        
        answer.append(obj[s])
        cnt += 1
        obj[s+m] = cnt
        s = ''
         
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
