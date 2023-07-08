import math

def solution(m, musicinfos):
    answer = ''
    answer_m = 0
    obj = {'C#':'c', 'D#':'d', 'F#':'f', 'G#':'g', 'A#':'a'}
    
    for key in obj.keys():
        m = m.replace(key, obj[key])
    
    for music in musicinfos:
        arr = music.split(',')
        start = arr[0].split(':')
        end = arr[1].split(':')
        name = arr[2]
        code = arr[3]
        
        end_m = int(end[0]) * 60 + int(end[1])
        start_m = int(start[0]) * 60 + int(start[1])
        
        minute = end_m - start_m
        
        for key in obj.keys():
            code = code.replace(key, obj[key])
        
        size = len(code)
        total = code * (minute//size)
        total += code[:minute%size]
        
        if m in total:      
            if answer == '' or minute > answer_m :
                answer = name
                answer_m = minute
        
    if answer == '':
        answer = '(None)'
        
    return answer