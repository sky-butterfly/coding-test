def solution(score):
    answer = []
    obj = {}
    score_list = []
    
    for i, s in enumerate(score):
        add = sum(s)
        ave = 0
        if add != 0:
            ave = add/2
        
        obj[str(i)] = ave
        score_list.append(ave)
    
    score_list.sort(reverse=True)  

    pre_ave = score_list[0]
    for i, s in enumerate(score):
        ave = obj[str(i)]
        
        if i > 0:
            if ave == pre_ave:
                answer.append(answer[i-1])
            else:
               answer.append(score_list.index(ave)+1)   
        else:
            answer.append(score_list.index(ave)+1)   
            
        pre_ave = ave
    
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges