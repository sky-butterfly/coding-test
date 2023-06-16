def solution(chicken):
    answer = int(chicken/10)
    coopon = answer + chicken%10
    
    while(coopon > 9) : 
        answer += int(coopon/10)        
        coopon = int(coopon/10) + coopon%10
    
    return answer