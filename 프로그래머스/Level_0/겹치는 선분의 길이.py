def solution(lines):
    answer = 0
    result = []
    arr = []
    
    lines.sort()
    
    for l in lines:
        for i in range(l[0], l[1]):
            
            if [i, i+1] in arr:                
                if [i, i+1] in result:
                    continue
                result.append([i, i+1])                
                answer += 1
            else:
                arr.append([i, i+1])
    
    return answer