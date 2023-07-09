from itertools import permutations

def solution(n, k):
    answer = []
    m = n
    
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    
    obj = {}
    
    for i in range(1, n+1):
        v = 0
        if i == 1:
            v = 1
        else:
            v = obj[i-1] * i
        obj[i] = v
    
    for i in range(n-1, 0, -1):
        cnt = obj[i]
        
        v = k//cnt
        add = k%cnt
        if add > 0:
            v += 1
            
        answer.append(arr[v-1])
        arr.remove(arr[v-1])
        
        k = add
        
    answer.append(arr[0])
    
    return answer


# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges