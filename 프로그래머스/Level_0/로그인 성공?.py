def solution(id_pw, db):
    answer = 'fail'
    id_obj = {}
    
    for d in db:
        id_obj[d[0]] = d[1]
    
    if id_pw[0] in id_obj.keys():
        if id_pw[1] == id_obj[id_pw[0]]:
            answer = 'login'
        else:
            answer = 'wrong pw'
    
    return answer