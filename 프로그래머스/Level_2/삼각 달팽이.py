def solution(n):
    
    obj = {0:(1, 0), 1:(0, 1), 2:(-1, -1)}
    arr = []
    x, y, num = -1, 0, 1
    
    for i in range(1, n+1):
        arr.append([0]*i)
    
    for i in range(n, -1, -1):
        for j in range(i):
            
            add_x, add_y = obj[(n-i)%3]
            x += add_x
            y += add_y
            
            arr[x][y] = num
            num += 1
    

    return sum(arr, [])

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges