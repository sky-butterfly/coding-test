def solution(players, callings):
    answer = []
    obj = { p : i for i, p in enumerate(players)}
    
    for c in callings:
        pre, index = obj[c]-1, obj[c]
        
        players[index] = players[pre]
        players[pre] = c
        
        obj[c] = obj[c]-1
        obj[players[index]] = obj[players[index]]+1
        
    return players