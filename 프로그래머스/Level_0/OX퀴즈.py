def solution(quiz):
    answer = []
    
    for q in quiz:
        
        arr = q.split(' ')
        s = ''
        x = 0
        
        for a in arr:
            
            if a.isdigit() == False and len(a) == 1:
                s = a
                continue
            
            i = 0
            if a.startswith('-'):
                i = (-1 * int(a[1:]))
            else:
                i = int(a)
            
            if s == '' or s == '+':
                x += i
                continue
            if s == '-':
                x -= i
                continue
            
            if i == x:
                answer.append('O')
            else:
                answer.append('X')
    
    return answer