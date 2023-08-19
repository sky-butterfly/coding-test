def solution(k, ranges):
    answer = []
    
    x = 0
    obj = {x:k}
    arr = [[x, k]]
    while k > 1:
        
        if k%2 == 0:
            k = k//2
        else:
            k = k*3 + 1
        
        x += 1
        
        arr.append([x, k])
        obj[x] = k
        
    area_list = []
    for i in range(len(arr)-1):
        
        a1 = arr[i]
        a2 = arr[i+1]
        
        area_list.append(((a1[1] + a2[1]) * (a2[0] - a1[0]))/2)
    
    size_x = arr[len(arr)-1][0]
    for r in ranges:
        if r[0] > size_x + r[1]:
            answer.append(-1)
            continue
        
        x1 = r[0]
        x2 = size_x + r[1]
        result = 0
        for a in range(x1, x2):
            result += area_list[a]
            
        answer.append(result)
        
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges