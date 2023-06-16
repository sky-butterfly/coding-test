def solution(arr, idx):
    
    sArr = list(map(str, arr[idx:]))
    arr = (''.join(sArr)).split('01')
    
    if '1' in arr[0]:
        return idx
    
    if len(arr) == 1:
        return -1

    return idx + len(arr[0]) + 1