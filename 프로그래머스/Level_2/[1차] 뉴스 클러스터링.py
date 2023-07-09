import math

def solution(str1, str2):
    answer = 0
    start = ord('a')
    end = ord('z')
    
    arr1 = []
    for i in range(len(str1)-1):
        a = str1[i:i+2]
        a = a.lower() 
        if ord(a[0]) < start or ord(a[0]) > end:
            continue
        if ord(a[1]) < start or ord(a[1]) > end:
            continue
        arr1.append(a)
    
    arr2 = []
    for i in range(len(str2)-1):
        a = str2[i:i+2]
        a = a.lower()
        if ord(a[0]) < start or ord(a[0]) > end:
            continue
        if ord(a[1]) < start or ord(a[1]) > end:
            continue
        arr2.append(a)
        
    x = []
    y = []
    i = 0
    while len(arr1) > 0:
        a = arr1[0]
        if (a in arr2) == False:
            y.append(a)
            arr1.pop(0)
            continue
        cnt1 = arr1.count(a)
        cnt2 = arr2.count(a)
        
        mn_cnt = min(cnt1, cnt2)
        mx_cnt = max(cnt1, cnt2)
        for i in range(1, mx_cnt+1):
            if i <= mn_cnt:
                x.append(a)
            y.append(a)
        arr1 = [i for i in arr1 if i != a]
        arr2 = [i for i in arr2 if i != a]
            
    for a in arr2:
        y.append(a)
    
    if x == [] and y == []:
        answer = 1
    elif x == [] or y == []:
        return 0
    else :
        answer = len(x) / len(y)
    
    return math.trunc(answer*65536)

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges