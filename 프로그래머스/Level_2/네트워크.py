def solution(n, computers):
    answer = 0
    check = []
    
    for i in range(n):
        if i not in check:
            check.append(i)
            answer += 1
            dfs(i, computers, check, n)
    
    return answer

def dfs(i, computers, check, n):
    for j in range(n):
        if computers[i][j] == 1 and j not in check:
            check.append(i)
            dfs(j, computers, check, n)

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges