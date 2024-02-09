def solution(grid):
    answer = []
    
    x_last = len(grid)-1
    y_last = len(grid[0])-1
    
    start_end_arr = set()
    for i in range(x_last+1):
        for k in range(y_last+1):
            start_end_arr.add((i,k,i+1,k))
            start_end_arr.add((i, k, i-1, k))
            start_end_arr.add((i, k, i, k+1))
            start_end_arr.add((i, k, i, k-1))
    
    check_all = set()
    for start_end in start_end_arr:
        start_x, start_y, end_x, end_y = start_end
        start = [start_x, start_y]
        end = [end_x, end_y]
        if (start[0], start[1], end[0], end[1]) in check_all:
            continue
        
        index = 0
        while (start[0], start[1], end[0], end[1]) not in check_all:
            index += 1
            check_all.add((start[0], start[1], end[0], end[1]))
            
            if end[0] > x_last:
                end[0] = 0
                start[0] = -1
            elif end[0] < 0:
                end[0] = x_last
                start[0] = x_last+1
            elif end[1] > y_last:
                end[1] = 0
                start[1] = -1
            elif end[1] < 0:
                end[1] = y_last
                start[1] = y_last+1
                
            next_word = [end[0], end[1]]
            word = grid[next_word[0]][next_word[1]]
            if word == 'S':
                if end[0]-start[0] == 1:
                    next_word[0] += 1
                elif end[0]-start[0] == -1:
                    next_word[0] -= 1
                elif end[1]-start[1] == 1:
                    next_word[1] += 1
                else:
                    next_word[1] -= 1
            elif word == 'L':
                if end[0]-start[0] == 1:
                    next_word[1] += 1
                elif end[0]-start[0] == -1:
                    next_word[1] -= 1
                elif end[1]-start[1] == 1:
                    next_word[0] -= 1
                else:
                    next_word[0] += 1
            else:
                if end[0]-start[0] == 1:
                    next_word[1] -= 1
                elif end[0]-start[0] == -1:
                    next_word[1] += 1
                elif end[1]-start[1] == 1:
                    next_word[0] += 1
                else:
                    next_word[0] -= 1 
            
            start = [end[0], end[1]]
            end = [next_word[0], next_word[1]]
            
        answer.append(index)
    answer.sort()
    return answer


# 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges