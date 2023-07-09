from collections import deque

def solution(n, wires):
    answer = n
    
    for i in range(len(wires)):
        cnt = 0
        if i == 0:
            cnt = check(wires[i+1:])
        elif i == len(wires)-1:
            cnt = check(wires[:i])
        else:   
            cnt = check(wires[:i] + wires[i+1:])
        
        if answer > abs(n-cnt-cnt):
            answer = abs(n-cnt-cnt)
    
    return answer

def check(wires):
    cnt = 1
    queue = deque()
    queue.append(wires[0][0])
    
    while queue:
        q = queue.popleft()   
        w_arr = []
        for w in wires:
            
            if q == w[0]:
                queue.append(w[1])
                cnt += 1
                w_arr.append(w)
            elif q == w[1]:
                queue.append(w[0])
                cnt += 1
                w_arr.append(w)
                
        for w in w_arr:
            wires.remove(w)
                
    return cnt

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges