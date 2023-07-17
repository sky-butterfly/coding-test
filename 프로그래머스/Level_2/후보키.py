from itertools import combinations

def solution(relation):    
    answer_arr = []
    row_size = len(relation)
    col_size = len(relation[0])
    col_index = []
    for i in range(col_size):
        col_index.append(i)
    
    num = 1
    while num < len(col_index)+1:
        
        com = map(list, combinations(col_index, num))
        
        for c in com:
            arr = []
            for r in relation:
                a = []
                for cc in c:
                    a.append(r[cc])
                
                if a not in arr:
                    arr.append(a)
            
            if row_size == len(arr):
                answer_arr.append(c)
                # if len(c) == 1:
                #     col_index.remove(c[0])
            
        num += 1
        
    delete_arr = []
    for i in range(len(answer_arr)):
        for j in range(len(answer_arr)):
            if i == j:
                continue
            s_i = set(answer_arr[i])
            s_j = set(answer_arr[j])
            if s_i.issubset(s_j) and answer_arr[j] not in delete_arr:
                delete_arr.append(answer_arr[j])
    
    for da in delete_arr:
        answer_arr.remove(da)
    
    answer_arr.sort(reverse=True)
    
    return len(answer_arr)
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges