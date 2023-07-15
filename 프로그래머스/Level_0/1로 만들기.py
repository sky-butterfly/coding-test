def solution(num_list):
    answer = 0
    
    for n in num_list:
        while(n > 1):
            answer += 1
            
            if n%2 == 0:
                n /= 2
            else :
                n -= 1
                n /= 2
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges