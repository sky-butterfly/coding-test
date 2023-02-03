function solution(s){    
    var answer = true;    

    var check = 0;
    
    for(var i=0; i<s.length; i++){
        
        var a = s.substring(i, i+1);
        
        if(a == '('){
            check++;
            continue;
        }
        
        check--;
        if(check < 0){
            return false;
        }
    }
    
    if(check != 0){
        answer = false;
    }

    return answer;
}
