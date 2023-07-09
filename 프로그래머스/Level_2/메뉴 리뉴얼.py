from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        
        obj = {}
        mx = 0
        
        for o in orders:
            for li in combinations(o, c):
                l = sorted(list(li))
                key = ''.join(l)
                
                num = obj.get(key, 0)
                num += 1
                obj[key] = num
                
                if mx < num:
                    mx = num
                    
        for o in obj:
            if mx > 1 and obj[o] == mx:
                answer.append(o)
    
    return sorted(answer)

# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges