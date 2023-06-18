def solution(wallpaper):
    answer = []
    x = []
    y = []
    
    for i, wall in enumerate(wallpaper):
        for j, w in enumerate(wall):
            if w == '#':
                if (i in x) == False:
                    x.append(i)
                if (j in y) == False:
                    y.append(j)
                
    x.sort()
    y.sort()
    answer.append(x[0])
    answer.append(y[0])
    
    rdx = x[len(x)-1]+1
    rdy = y[len(y)-1]+1
        
    answer.append(rdx)
    answer.append(rdy)
    
    return answer