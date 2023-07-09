from collections import Counter, deque

def solution(arr):
    answer = [0, 0]
    queue = deque()
    queue.append(arr)
    
    while queue:
        aa = queue.popleft()
        dict_counter = {}
        
        for a in aa:
            counter = Counter(a)
            dict_counter.update(dict(counter))
        
        if len(dict_counter) > 1:

            size = len(aa)//2
            arr_1 = []
            arr_2 = []
            arr_3 = []
            arr_4 = []
            
            arr_1_2 = aa[:size]
            for a in arr_1_2:
                arr_1.append(a[:size])
                arr_2.append(a[size:])
            arr_3_4 = aa[size:]
            for a in arr_3_4:
                arr_3.append(a[:size])
                arr_4.append(a[size:])
            
            queue.append(arr_1)
            queue.append(arr_2)
            queue.append(arr_3)
            queue.append(arr_4)
        else:
            num = list(dict_counter.keys())[0]
            answer[num] += 1
        
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
    