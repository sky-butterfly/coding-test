def solution(keymap, targets):
    answer = []
    A = ord('A')
    obj = {}
    
    for i in range(ord('A'), ord('Z')+1):
        s = chr(i)
        for j, k in enumerate(keymap):
            if (s in k) == False:
                continue
            index = k.index(s)
            if s in obj.keys():
                num = obj[s]
                if num > index+1:
                    obj[s] = index+1
                continue  
            obj[s] = index+1
    
    for ta in targets:
        add = 0
        for t in ta:
            if t in obj.keys():
                add += obj[t]
            else:
                add = -1
                break
                
        if add == 0:
            add = -1
            
        answer.append(add)
    
    return answer