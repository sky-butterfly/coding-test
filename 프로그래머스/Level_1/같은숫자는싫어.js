function solution(arr)
{
    var answer = [];

    var before = arr[0];
    answer[0] = (before);
    
    for(var i=0; i<arr.length; i++){
        var a = arr[i];
        
        if(a == before){
            continue;
        }
        
        answer[answer.length] = a;
        before = a;
    }
    
    return answer;
}
