function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    var size = truck_weights.length;
    
    var trucks = Array.from({length:bridge_length}, () => 0);
    var done = [];
    var totalWeights = 0;
    
    while(done.length < size){
        answer++;
        
        var t = trucks.shift();
        totalWeights -= t;
        
        if(t > 0){
            done.push(t);
        }
        
        if(truck_weights.length > 0 && totalWeights+truck_weights[0] <= weight){
            var tw = truck_weights[0];
            trucks.push(truck_weights.shift());
            totalWeights += tw;
        }else{
            trucks.push(0);
        }
    }
    
    return answer;
}
