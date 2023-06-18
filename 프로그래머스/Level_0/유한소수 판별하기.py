import fractions

def solution(a, b):
    answer = 2
    
    x = fractions.Fraction(a, b)
    b = x.denominator
    if b == 1:
        return 1
    
    arr = []
    i = 0
    while i <= b//2:
        i += 1
        if i in arr:
            continue
        if b%i == 0:
            if i != 1:
                arr.append(i)
            arr.append(b//i)
    
    arr.sort()
    index = 0
    while index < len(arr):
        a = arr[index]
        if a == 1:
            index += 1
            continue
        arr = [j for j in arr if j == a or j%a != 0]
        index += 1
    
    # if len(arr) > 0:
    #     if 2 in arr:
    #         arr.remove(2)
    #     if 5 in arr:
    #         arr.remove(5)
    #     if len(arr) < 1:
    #         answer = 1
    temp = [i for i in arr if i == 2 or i == 5]
    if len(temp) > 0:
        temp2 = [i for i in arr if i != 2 and i != 5]
        print(temp2)
        if len(temp2) < 1:
            answer = 1
        
    return answer