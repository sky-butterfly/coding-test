def solution(park, routes):
    answer = [0, 0]
    w = len(park[0])-1
    h = len(park)-1
    
    for i, pa in enumerate(park):
        for j, p in enumerate(pa):
            if p == 'S':
                answer[0] = i
                answer[1] = j
                break
    
    for r in routes:
        exist = False
        arr = r.split(' ')
        x = answer[1]
        y = answer[0]
        if arr[0] == 'E':
            new_x = x+int(arr[1])
            if new_x > w:
                continue
            new_x = x
            for i in range(1, int(arr[1])+1):
                new_x += 1
                if park[y][new_x] == 'X':
                    exist = True
                    break
            if exist == False:
                x = new_x
            answer[1] = x
            continue
        
        if arr[0] == 'S':
            new_y = y + int(arr[1])
            if new_y > h:
                continue
            new_y = y
            for i in range(1, int(arr[1])+1):
                new_y += 1
                if park[new_y][x] == 'X':
                    exist = True
                    break
            if exist == False :
                y = new_y
            answer[0] = y
            continue
        
        if arr[0] == 'W':
            new_x = x - int(arr[1])
            if new_x < 0:
                continue
            new_x = x
            for i in range(1, int(arr[1])+1):
                new_x -= 1
                if park[y][new_x] == 'X':
                    exist = True
                    break
            if exist == False:
                x = new_x
            answer[1] = x
            continue
        
        if arr[0] == 'N':
            new_y = y - int(arr[1])
            if new_y < 0:
                continue
            new_y = y
            for i in range(1, int(arr[1])+1):
                new_y -= 1
                if park[new_y][x] == 'X':
                    exist = True
                    break
            if exist == False :
                y = new_y
            answer[0] = y
            continue
    
    return answer