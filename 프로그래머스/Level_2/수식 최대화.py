from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    
    arr = []
    n_a = []
    symbol = []
    num = ''
    for e in expression:
        
        if e.isdigit():
            num += e
        else:
            symbol.append(e)
            if e not in arr:
                arr.append(e)
            n_a.append(int(num))
            num = ''
    n_a.append(int(num))
    per = list(permutations(arr))
    
    for p in per:
        num_arr = n_a
        result = 0
        rank = list(p)
        s_stack = deque(symbol)
        while rank:
            stack = deque()
            r = rank.pop(0)
            for i, n in enumerate(num_arr):
                if i == 0:
                    stack.append(n)
                    continue
                if len(s_stack) < 1:
                    break
                s = s_stack.popleft()
                if s == r:
                    ss = stack.pop()
                    if s == '+':
                        result = ss + n
                    elif s == '-':
                        result = ss - n
                    else:
                        result = ss * n
                    
                    stack.append(result)
                else:
                    stack.append(n)
                    s_stack.append(s)
                    continue
                
                if s not in symbol:
                    break
        
            num_arr = list(stack)
        
        if answer < abs(result) :
            answer = abs(result)
                    
    return abs(answer)