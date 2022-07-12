def solution(numbers, hand):
    answer = []
    
    leftArr = [1, 4, 7]
    rightArr = [3, 6, 9]
    pad = [[1,0], [0,3], [1,3], [2,3], [0,2], [1,2], [2,2], [0,1], [1,1], [2,1]]
    leftHand = [0,0]
    rightHand = [2,0]
    
    for n in numbers:
        
        if n in leftArr:
            answer.append('L')
            leftHand = pad[n]

        elif n in rightArr:
            answer.append('R')
            rightHand = pad[n]
        
        else:
            leftDistance = abs(leftHand[0] - pad[n][0]) + abs(leftHand[1] - pad[n][1])
            righDistance = abs(rightHand[0] - pad[n][0]) + abs(rightHand[1] - pad[n][1])

            distance = leftDistance - righDistance
            if distance > 0 :
                answer.append('R')
                rightHand = pad[n]
            elif distance < 0 :
                answer.append('L')
                leftHand = pad[n]
            else :
                if hand == 'right':
                    answer.append('R')
                    rightHand = pad[n]
                else :
                    answer.append('L')
                    leftHand = pad[n]

    return ''.join(answer)
