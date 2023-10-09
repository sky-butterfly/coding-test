from itertools import combinations
from bisect import bisect_left, bisect_right

def solution(info, query):
    answer = []
    obj = {}
    
    combi = []
    for ii in range(4, -1, -1):
        for c in list(combinations([0, 1, 2, 3], ii)):
            combi.append(c)
    
    for index, i in enumerate(info):
        
        arr = i.split(' ')
        l = arr[0]
        j = arr[1]
        c = arr[2]
        f = arr[3]
        s = int(arr[4])
        
        str_list = [l, j, c, f]
        for com in combi:
            sl = ''
            for c in com:
                sl += str_list[c]
                
            a = obj.get(sl, [])
            a.append(s)
            obj[sl] = a
            
    for key in obj.keys():
        arr = obj[key]
        arr.sort()
        obj[key] = arr
            
    for q in query:
        
        arr = q.split(' and ')
        l = arr[0]
        j = arr[1]
        c = arr[2]
        arr_2 = arr[3].split(' ')
        f = arr_2[0]
        s = int(arr_2[1])
        
        q_str = ''
        
        if l != '-':
            q_str += l
        if j != '-':
            q_str += j
        if c != '-':
            q_str += c
        if f != '-':
            q_str += f
            
        result = obj.get(q_str, [])
        answer.append(len(result)-bisect_left(result, s))
        
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges