def solution(babbling):
    answer = 0
    arr = ['aya', 'ye', 'woo', 'ma']
    
    for b in babbling:
        for a in arr:
            if a in b:
                b = b.replace(a, ' ')
        if len(b.strip()) == 0:
            answer += 1
    
    return answer