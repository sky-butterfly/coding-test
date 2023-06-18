def solution(cards1, cards2, goal):
    answer = 'No'
    
    while answer == 'No':
        
        if len(goal) < 1:
            answer = 'Yes'
            break
        
        if len(cards1) < 1 and len(cards2) < 1:
            break
        
        g = goal[0]
        
        if len(cards1) > 0 and g == cards1[0]:
            goal.pop(0)
            cards1.pop(0)
            continue
        elif len(cards2) > 0 and g == cards2[0]:
            goal.pop(0)
            cards2.pop(0)
            continue
        else:
            break
    
    return answer