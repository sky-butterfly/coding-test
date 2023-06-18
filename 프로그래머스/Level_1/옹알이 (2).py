def solution(babbling):
    answer = 0
    arr = ['aya', 'ye', 'woo', 'ma']
    
    for babb in babbling:
        
        ok = False
        pre = ''
        word = ''
        for b in babb:
            word += b
            
            if word in arr:
                ok = True
                
                if pre == word:
                    ok = False
                    break
                pre = word
                word = ''
        if word != '':
            ok = False
        if ok :
            answer += 1
    
    return answer