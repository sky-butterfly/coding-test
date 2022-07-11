def solution(new_id):
    answer = []
    allow = ['-', '_', '.']
    
    for n in new_id :
        # 1단계
        if n.isupper():
            n = n.lower()
        # 2단계
        if (not n.isdigit()) and (not n.islower()) and (not n in allow):
            continue
        
        # 3단계
        if n == '.' and (len(answer) == 0 or answer[len(answer)-1] == '.'):
            continue            
        
        answer.append(n)
        
    while len(answer) > 0:            
        # 4단계
        n = answer[len(answer)-1]
        if n == '.':
            if len(answer) == 1:
                answer = []
            else:
                answer = answer[:len(answer)-1]
        else:
            break
    
    # 5단계
    if len(answer) < 1:
        answer.append('a')
            
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        while len(answer) > 0:   
            # 4단계
            n = answer[len(answer)-1]
            if n == '.':
                if len(answer) == 1:
                    answer = []
                else:
                    answer = answer[:len(answer)-1]
            else:
                break
    
    # 7단계
    if len(answer) < 3:
        n = answer[len(answer)-1]
        while len(answer) < 3:
            answer.append(n)
    
    return ''.join(answer)
