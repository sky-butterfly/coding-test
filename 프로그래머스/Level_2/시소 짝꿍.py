from collections import defaultdict

def solution(weights):
    answer = 0
    
    info = defaultdict(int)

    for w in weights:
        answer += info[w]
        answer += info[(w * 2) / 3] + info[(w * 3) / 2]
        answer += info[(w * 3) / 4] + info[(w * 4) / 3]
        answer += info[(w * 4) / 2] + info[(w * 2) / 4]
        info[w] += 1
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges