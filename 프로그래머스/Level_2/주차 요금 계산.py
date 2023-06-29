from datetime import datetime
import datetime as dt
import math

def solution(fees, records):
    answer = []
    basic_time = fees[0]
    basic_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]
    obj = {}
    
    for r in records:
        arr = r.split(' ')
        num = int(arr[1])
        
        if num in obj.keys():
            tmp = obj[num]
            tmp.append(arr)
            obj[num] = tmp
        else:
            obj[num] = [arr]
    
    keys = sorted(obj)
    
    for k in keys:
        time_obj = {}
        
        for a in obj[k]:
            t = datetime.strptime(a[0], '%H:%M')
            time_obj[t] = a[2]
        
        time_keys = sorted(time_obj)
        in_time = time_keys[0]
        complete = False
        result = 0
        total_time = 0
        for tk in time_keys:
            if time_obj[tk] == 'IN':
                in_time = tk
                complete = False
            else:
                complete = True
                out_time = tk
                total_time += ((out_time - in_time).seconds)/60
                
                
        if complete == False:
            out_time = datetime.strptime('23:59', '%H:%M')
            total_time += ((out_time - in_time).seconds)/60
        
        if total_time <= basic_time:
            result += basic_fee
        else:
            total_time -= basic_time
            result += basic_fee
            result += (math.ceil(total_time/per_time)*per_fee)
        answer.append(result)
                
    
    return answer