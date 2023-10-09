from collections import deque

def solution(name):
    answer = 0
    Z = ord('Z')
    A = ord('A')
    s = 'string'
    n = 'num'
    
    queue = deque()
    queue.append(('A'*len(name), 0, 0, [{s:'A'*len(name), n:0}]))
    
    while queue:
        string, index, count, history = queue.popleft()
        
        if string == name:
            answer = count
            break
        
        up = 0
        down = 0
        if ord(string[index]) < ord(name[index]):
            up = ord(name[index]) - ord(string[index])
            down = ( ord(string[index]) - A ) + ( Z - ord(name[index]) ) + 1
            
        if ord(string[index]) > ord(name[index]):
            down = ord(string[index]) - ord(name[index])
            up = ( Z - ord(string[index]) ) + ( ord(name[index]) - A ) + 1
                
        mn = min(up, down)

        if mn > 0:
            new_string = string[:index] + name[index]
            if index < len(name)-1:
                new_string += string[index+1:]

            obj = {s:new_string, n:index}
            if obj not in history:
                history.append(obj)
                queue.append((new_string, index, count+mn, history))
        
        left = index - 1
        if left < 0:
            left = len(name)-1
        
        obj = {s:string, n:left}
        if obj not in history:
            history.append(obj)
            queue.append((string, left, count+1, history))
        
        right = index + 1
        if right == len(name):
            right = 0
        
        obj = {s:string, n:right}
        if obj not in history:
            history.append(obj)
            queue.append((string, right, count+1, history))
        
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges