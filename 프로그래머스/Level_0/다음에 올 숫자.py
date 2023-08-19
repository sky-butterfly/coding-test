def solution(common):
    answer = 0
    size = len(common)
    x = common[1] - common[0]
    y = 0
    if common[1] != 0 and common[0] != 0:
        y = common[1] / common[0]
        
    flag = True
    
    for i in range(2, size):
        
        if i > 5:
            break
        
        diff = common[i] - common[i-1]
        if x != diff:
            flag = False
            break
            
    if flag :
        answer = common[size-1] + x
    else:
        answer = common[size-1] * y
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges