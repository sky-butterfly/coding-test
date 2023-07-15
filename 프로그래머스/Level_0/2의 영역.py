def solution(arr):
    answer = []
    
    if (2 in arr) == False:
        return [-1]
    
    for i, a in enumerate(arr):
        if a == 2:
            answer.extend(arr[i:])
            break
    
    for i in range(len(answer)-1, -1, -1):
        if answer[i] == 2:
            answer = answer[:i+1]
            break
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges