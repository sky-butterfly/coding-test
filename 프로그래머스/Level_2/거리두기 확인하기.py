def solution(places):
    answer = []
    
    for place in places:
        
        for i, p in enumerate(place):
            finish = False
            for j, pp in enumerate(p):
                
                if pp == 'X':
                    continue
                
                count = 0
                if i > 0:
                    if place[i-1][j] == 'P':
                        count += 1
                if i < len(place)-1:
                    if place[i+1][j] == 'P':
                        count += 1
                if j > 0:
                    if place[i][j-1] == 'P':
                        count += 1
                
                if j < len(p)-1:
                    if place[i][j+1] == 'P':
                        count += 1
                
                if pp == 'O' and count > 1:
                    answer.append(0)
                    finish = True
                    break
                    
                if pp == 'P' and count > 0:
                    answer.append(0)
                    finish = True
                    break
            
            if finish:
                break
                
        if finish == False:
            answer.append(1)
                
        
    return answer
    
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges