def solution(dartResult):
    answer = 0
    arr = []
    
    beforeIsDigit = False
    score = ''
    for d in dartResult:
        if d.isdigit():
            if beforeIsDigit == False:
                arr.append(score)
                score = ''
            score += d
            beforeIsDigit = True
            continue
            
        score += d
        beforeIsDigit = False

    arr.append(score)
    print(arr)
    score_list = []
    for a in arr:
        score_list.append(0)
    
    for i, a in enumerate(arr):
        num_str = ''
        num = -1
        for s in a:
            if s.isdigit():
                num_str += s
                continue
            if num < 0:
                num = int(num_str)
            if s == 'S':
                num = num**1
            elif s == 'D':
                num = num**2
            elif s == 'T':
                num = num**3
            elif s == '*':
                num = num*2
                if i > 0:
                    score_list[i-1] = score_list[i-1]*2
            elif s == '#':
                num = num*(-1)
                
            score_list[i] = num
    
    for sl in score_list:
        answer += sl
    
    return answer