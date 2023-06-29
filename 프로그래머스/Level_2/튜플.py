def solution(s):
    answer = []
    obj = {}
    
    s = s[2:len(s)-2]
    arr = s.split("},{")
    
    for a in arr:
        aa = a.split(',')
        obj[len(aa)] = aa
    
    for i in range(1, len(arr)+1):
        aa = obj[i]
        for a in aa:
            if (int(a) in answer) == False:
                answer.append(int(a))
                break
    
    return answer