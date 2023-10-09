from collections import deque

def solution(n, info):
    answer = []
    max_num = 0
    start_peach = 0
    arr = []
    
    for j in range(11):
        
        queue = deque()
        queue.append((0, j, n, [0]*11))
    
        while queue:
            lion, start, count, check = queue.popleft()
                
            if start > 10:
                peach = 0
                for ii in range(11):
                    if info[ii] > 0 and info[ii] > check[ii]:
                        peach += 10-ii
                
                if peach < lion :
                    if max_num < lion-peach and check not in arr:
                        arr.append(check)
                        max_num = lion-peach
                        answer = [c for c in check]
                    elif max_num == lion-peach and check not in arr:
                        for i in range(10, -1, -1):
                            if check[i] > answer[i]:
                                arr.append(check)
                                max_num = lion-peach
                                answer = [c for c in check]
                                break
                continue
            
            for i in range(start, 11):

                new_lion = lion
                new_count = count
                new_check = [c for c in check]
                
                if new_count > info[i]:
                    new_lion += (10-i)
                    
                    if i == 10:
                        new_check[i] = new_count
                        new_count = 0
                    else:
                        new_count -= (info[i]+1)
                        new_check[i] = (info[i]+1)
                
                elif i == 10:
                    new_check[i] = new_count
                    new_count = 0
                    
                queue.append((new_lion, i+1, new_count, new_check))
    
    if max_num == 0:
        answer = [-1]
    
    return answer


# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
        
        