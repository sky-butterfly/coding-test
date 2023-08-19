from collections import deque

def solution(plans):
    answer = []
    queue = []
    
    stack = deque()
    
    for p in plans:
        
        name = p[0]
        start = p[1].split(':')
        playtime = p[2]
        
        start_h = int(start[0])
        start_m = int(start[1])
        
        queue.append({'name':name, 'start_h':start_h, 'start_m':start_m, 'playtime':int(playtime)})
    
    queue.sort(key=lambda x: 60*x['start_h']+x['start_m'])
    curr_h = queue[0]['start_h']
    curr_m = queue[0]['start_m']
    curr = queue.pop(0)
    
    while queue:
        
        curr_playtime_sum = curr_m + curr['playtime']
        curr_end_h = curr_h + curr_playtime_sum // 60
        curr_end_m = curr_playtime_sum % 60
        
        q = queue[0]
        
        compare = dateCompare(curr_end_h, curr_end_m, q['start_h'], q['start_m'])
        if compare == 1:
            
            diff_h = q['start_h'] - curr_h
            diff_m = 60*diff_h + (q['start_m'] - curr_m)
            diff_time = curr['playtime'] - diff_m
            curr['playtime'] = diff_time
            
            stack.append(curr)
            curr = queue.pop(0)
            curr_h = curr['start_h']
            curr_m = curr['start_m']
            continue
        
        if compare == 0:
            answer.append(curr['name'])
            curr = queue.pop(0)
            curr_h = curr['start_h']
            curr_m = curr['start_m']
            continue
            
        if compare == -1:
            answer.append(curr['name'])
            
            if stack:
                curr = stack.pop()
                curr_h = curr_end_h
                curr_m = curr_end_m
            else:
                curr = queue.pop(0)
                curr_h = curr['start_h']
                curr_m = curr['start_m']
                
    answer.append(curr['name'])
    
    while stack:
        answer.append(stack.pop()['name'])
        
    return answer

def dateCompare(a_h, a_m, b_h, b_m):
    
    if a_h > b_h:
        return 1
    
    if a_h < b_h:
        return -1
    
    if a_m > b_m:
        return 1
    
    if a_m < b_m:
        return -1
    
    return 0
    
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges