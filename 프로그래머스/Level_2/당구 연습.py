import math

def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        
        result = -1
        bx = ball[0]
        by = ball[1]
        
        x = startX
        y = startY
        
        if (bx-x) == (by-y):
            start_line = 0
            ball_line = 0
            if (bx-x) > 0:
                if (by-y) > 0:   
                    start_line = x**2 + y**2
                    ball_line = bx**2 + by**2
                else:
                    start_line = x**2 + (n-y)**2
                    ball_line = bx**2 + (n-by)**2
            else:
                if (by-y) > 0:
                    start_line = (m-x)**2 + y**2
                    ball_line = (m-bx)**2 + by**2
                else:
                    start_line = (m-x)**2 + (n-y)**2
                    ball_line = (m-bx)**2 + (n-by)**2
            
            result = start_line + ball_line
        
        y_line = abs(y-by)/2
        if (y == by and (x-bx) > 0) == False:
            left = (bx+x)**2 + abs(by-y)**2
            if result == -1 or left < result:
                result = left
        if (y == by and (bx-x) > 0) == False:
            right = ((m-x)+(m-bx))**2 + abs(by-y)**2
            if result == -1 or right < result:
                result = right
        x_line = abs(x-bx)/2
        if (x == bx and (by-y) > 0) == False:
            top = abs(bx-x)**2 + ((n-y)+(n-by))**2
            if result == -1 or top < result:
                result = top
        if (x == bx and (y-by) > 0) == False:
            bottom = abs(bx-x)**2 + (y+by)**2
            if result == -1 or bottom < result:
                result = bottom
            
        answer.append(result)
    
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges