def solution(numbers, hand):
    answer = ''

    cursor = {'r' : [0,0], 'l' : [2,0]}
    phone = [[1,0], [0,3], [1,3], [2,3], [0,2], [1,2], [2,2], [0,1], [1,1], [2,1]]
    
    for n in numbers :

        if n == 1 or n == 4 or n == 7 :
            answer += 'L';
            cursor['l'] = phone[n]
        elif n == 3 or n == 6 or n == 9 :
            answer += 'R';
            cursor['r'] = phone[n]
        else:            
            p = phone[n]

            r = cursor['r']   
            rx = r[0]-p[0]
            ry = r[1]-p[1]
            if(ry < 0):
                ry = ry * -1
            
            l = cursor['l']
            lx = p[0] - l[0]
            ly = p[1] - l[1]
            if(ly < 0):
                ly = ly * -1
            
            if (rx+ry) > (lx+ly):
                answer += 'L';
                cursor['l'] = phone[n]
            elif (lx+ly) > (rx+ry):
                answer += 'R';
                cursor['r'] = phone[n]
            else :
                if hand == "right":
                    answer += 'R'
                    cursor['r'] = phone[n]
                else :
                    answer += 'L'
                    cursor['l'] = phone[n]              

    return answer

print(solution([1,3,4,5,8,2,1,4,5,9,5], "right"))