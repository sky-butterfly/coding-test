def solution(n, k):
    answer = 0
    
    x = get(n, k)
    
    s = ''
    for i in x:
        if i == '0' and s == '':
            continue
        
        if i != '0':
            s += i
            continue
        
        if i == '0':
            if check(s):
                answer += 1
            s = ''
            
    if s != '':
        if check(s):
            answer += 1
    
    return answer

def get(n, k):
    
    result = ''
    while n > (k-1):
        result += str(n%k)
        n = n//k
    result += str(n)
    
    l = list(result)
    l.reverse()
    
    return ''.join(l)

def check(n):
    result = True
    
    if n == '0' or n == '1':
        return False
    
    nn = int(n)
    num = int(nn**0.5)
    for i in range(2, num+1):
        if nn%i == 0:
            result = False
            break
            
    return result