def solution(array, n):
    answer = array[0]
    
    array.sort()
    
    aabs = abs(n-array[0])
    num = aabs
    
    for i in range(len(array)):
        a = array[i]
        
        aabs = abs(n-a)
        
        if(aabs < num):
            num = aabs
            answer = a
    
    return answer