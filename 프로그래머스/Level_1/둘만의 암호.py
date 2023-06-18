def solution(s, skip, index):
    answer = ''
    x = ord('z') - ord('a')
    if index > x:
        index = index%x
        
    for ss in s:
        a = ord(ss)
        for i in range(index):
            t = a+1
            while True:
                if chr(t) in skip :
                    t += 1
                    continue
                if t > ord('z'):
                    t = ord('a')
                    continue
                a = t
                break
                    
        answer += chr(a)
    
    return answer