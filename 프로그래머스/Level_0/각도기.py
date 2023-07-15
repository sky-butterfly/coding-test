def solution(angle):
    if(angle < 90):
        return 1
    
    if(angle == 90):
        return 2
    
    if(angle < 180):
        return 3
    
    return 4

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges