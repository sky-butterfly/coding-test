def solution(N, stages):
    answer = []
    obj = {}
    keys = []
    
    pass_person = 0
    for i in range(N+1, 0, -1):
        fail = 0
        stages_size = len(stages)
        hold_person = 0
        
        if stages_size > 0 :
            stages = [j for j in stages if j != i]
            hold_person = stages_size - len(stages)
        
        pass_person += hold_person
        if i == N+1:
            continue    
            
        fail = getFail(pass_person, hold_person)
        if fail in obj.keys():
            temp = obj[fail]
            temp.insert(0, i)
            obj[fail] = temp
            continue
        
        keys.append(fail)
        obj[fail] = [i]
    
    keys.sort(reverse=True)
    for k in keys:
        answer.extend(obj[k])
    
    return answer

def getFail(total, hold):
    if total == 0 or hold == 0:
        return 0
    return hold / total