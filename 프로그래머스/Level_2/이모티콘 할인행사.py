def solution(users, emoticons):
    answer = []
    size = len(emoticons)
    discount = [10, 20, 30, 40]
    arr = []
    
    def dfs(tmp, depth):
        
        if depth == size:
            arr.append(tmp[:])
            return
        
        for d in discount:
            tmp[depth] += d
            dfs(tmp, depth+1)
            tmp[depth] -= d
    
    dfs([0]*size, 0)
    
    for aa in arr:
        
        discount_arr = []
        
        for i, a in enumerate(aa):
            e = emoticons[i]
            e = e - int(e * (a/100))
            discount_arr.append(e)
        
        plus = 0
        get = 0
        for u in users:
            d = u[0]
            t = u[1]
            total = 0
            for i, a in enumerate(aa):
                if a >= d:
                    total += discount_arr[i]
                    
                if total >= t:
                    total = 0
                    plus += 1
                    break
            
            get += total
            
            if answer:            
                curr_plus = answer[0]
                curr_get = answer[1]
                
                if curr_plus < plus:
                    answer = [plus, get]
                    continue
                    
                if curr_plus == plus and curr_get < get:
                    answer = [plus, get]
                    continue
            else:
                answer = [plus, get]
                    
            
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges