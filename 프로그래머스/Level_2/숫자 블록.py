def solution(begin, end):
    answer = []
    
    for i in range(begin, end+1):
        
        if i == 1:
            answer.append(0)
            continue
        
        # if i % 2 == 0:
        #     answer.append(i//2)
        #     continue
        
        result = 1
        arr = []
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                if i//j <= 10000000:
                    result = i//j
                    break
                else:
                    arr.append(j)
                    
        if len(arr) > 0 and result == 1:
            if result == 1:
                result = arr.pop()
            
        answer.append(result)
        
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges