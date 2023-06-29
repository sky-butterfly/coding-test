def solution(files):
    answer = []
    
    arr = []
    for i, file in enumerate(files):
        file_lower = file.lower()
        head = ''
        str_number = ''
        
        for f in file_lower:
            if f.isdigit():
                str_number += f
                continue
            if str_number != '':
                break
            head += f
            
        arr.append([i, head, int(str_number)])
    
    arr = sorted(arr, key=lambda x: (x[1], x[2], x[0]))
    
    return [files[a[0]] for a in arr]