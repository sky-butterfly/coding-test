from collections import deque

def solution(sequence, k):
    answer = []
    
    sequence = [i for i in sequence if i <= k]
    
    add = 0
    index_arr = deque()
    count = 0
    answer_count = 0
    for i in range(len(sequence)-1, -1, -1):
        s = sequence[i]
        
        add += s
        count += 1
        index_arr.append(i)
        if answer_count > 0 and count > answer_count:
            break
        
        if add < k:
            continue
        
        if add == k :
            answer = [index_arr[-1], index_arr[0]]
            answer_count = count
        
        add -= sequence[index_arr[0]]
        index_arr.popleft()
        count -= 1
    
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges