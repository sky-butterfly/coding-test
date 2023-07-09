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


//출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges