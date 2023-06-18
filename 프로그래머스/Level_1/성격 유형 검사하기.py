def solution(survey, choices):
    answer = ''
    arr = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    obj = {}
    
    for a in arr:
        obj[a] = 0
    
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        
        if c == 1:
            obj[s[0]] = obj[s[0]] + 3
        elif c == 2:
            obj[s[0]] = obj[s[0]] + 2
        elif c == 3:
            obj[s[0]] = obj[s[0]] + 1
        elif c == 5:
            obj[s[1]] = obj[s[1]] + 1
        elif c == 6:
            obj[s[1]] = obj[s[1]] + 2
        elif c == 7:
            obj[s[1]] = obj[s[1]] + 3
    
    
    if obj['R'] > obj['T']:
        answer += 'R'
    elif obj['R'] < obj['T']:
        answer += 'T'
    else:
        answer += chr(min(ord('R'), ord('T')))
    
    if obj['C'] > obj['F']:
        answer += 'C'
    elif obj['C'] < obj['F']:
        answer += 'F'
    else:
        answer += chr(min(ord('C'), ord('F')))
    
    if obj['J'] > obj['M']:
        answer += 'J'
    elif obj['J'] < obj['M']:
        answer += 'M'
    else:
        answer += chr(min(ord('J'), ord('M')))
    
    if obj['A'] > obj['N']:
        answer += 'A'
    elif obj['A'] < obj['N']:
        answer += 'N'
    else:
        answer += chr(min(ord('A'), ord('N')))
        
    return answer