def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[0])
    
    arr = []
    for t in targets:
        
        s = t[0]
        e = t[1]
        
        check = False
        for i in range(len(arr)-1, -1 , -1):
            a = arr[i]
            
            if a[1] > s :
                check = True
                arr[i] = [s, min(e, a[1])]                
                break
                
        if check == False:
            arr.append([s, e])
    
    answer = len(arr)
                
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges