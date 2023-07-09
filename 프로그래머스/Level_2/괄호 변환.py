from collections import deque

def solution(p):
    answer = ''
    
    if p == '':
        return p
            
    return loof(deque(p))

def loof(v):
    
    result = ''
    
    u = deque()
    front = 0
    back = 0
    
    if check(v):
        return ''.join(v)
    
    while v:
        vv = v.popleft()
        u.append(vv)

        if vv == '(':
            front += 1
        else:
            back += 1

        if front > 0 and front == back:
            if check(u):
                result += ''.join(u)
                u.clear()
            else:
                break
    
    result += '('
    result += ''.join(loof(v))
    result += ')'

    u.popleft()
    u.pop()

    for uu in u:
        if uu == '(':
            uu = ')'
        else:
            uu = '('
        result += uu
    
    return result

def check(u):
    result = True
    
    stack = deque()
    for uu in u:
        if len(stack) < 1 :
            if uu == ')':
                result = False
                break
            stack.append(uu)
            continue
        
        s = stack[-1]
        if s == '(' and uu == ')':
            stack.pop()
            continue
            
        stack.append(uu)
            
    if len(stack) > 0:
        result = False
        
    return result

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges