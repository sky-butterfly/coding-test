function solution(priorities, location) {
    var answer = 0;
    var arr = priorities.map((value, index) => [value, index]);
    
    while(arr.length > 0){
        
        var curr = arr.shift();
        var flag = true;
        
        for(var i in arr){
            if(curr[0] < arr[i][0]){
                flag = false;
                arr.push(curr);
                break;
            }
        }
        
        if(flag){
            answer++;
            if(curr[1] == location){
                return answer;
            }
        }
        
    }
    return answer;
}


// 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges