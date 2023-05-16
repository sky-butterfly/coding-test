def solution(code):
    answer = ''
    mode = 0
    
    for i in range(len(code)):
        c = code[i]
        
        if mode == 0:
            if c == '1':
                mode = 1
                continue
            if i%2 == 0:
                answer += c
                continue
            continue
        if c == '1':
            mode = 0
            continue
        if i%2 == 1:
            print(i, c)
            answer += c
    
    
    if answer == '':
        answer = 'EMPTY'
    
    return answer
