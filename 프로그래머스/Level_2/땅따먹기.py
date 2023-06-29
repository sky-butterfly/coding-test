def solution(land):
    answer = 0
    obj = {}
    
    for i, l in enumerate(land):
        o = {}
        for ii, ll in enumerate(l):
            if i == 0:
                o[ii] = ll
                continue
            
            oo = obj[i-1]
            mx = 0
            for k in oo.keys():
                if k == ii:
                    continue
                num = oo[k] + ll
                if mx < num:
                    mx = num
                    o[ii] = mx
            
        obj[i] = o
    
    last_obj = obj[len(land)-1]
    for last in last_obj.keys():
        if answer < last_obj[last]:
            answer = last_obj[last]
        
        
    return answer