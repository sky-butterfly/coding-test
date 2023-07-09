function solution(board) {
    var answer = 1;
    
    var oNum = 0;
    var xNum = 0;
    var totalNum = board.length * board[0].length;
    var currentNum = 0;
    
    // 가로
    var horizontal = [];
    
    // 세로
    var vertical = [];
    var verticalCount = [];
    
    // 대각선
    var diagonal_1 = [];
    var diagonal_2 = [];
    
    // 종료
    var done = false;
    var doneStr = '.';
    
    for(var i=0; i<board.length; i++){
        horizontal = [];
        
        // 대각선
        diagonal_1[i] = board[i][board.length-1-i];
        diagonal_2[i] = board[i][i];
        
        for(var k=0; k<board[i].length; k++){
            
            var b = board[i][k];
            
            if(b == 'O'){
                oNum++;
            }else if(b == 'X'){
                xNum++;
            }else{
                if(i == 0){
                    vertical[k] = b;
                    verticalCount[k] = 0;
                }
                continue;
            }
            
            // 가로
            if(horizontal.length != 0 && horizontal[horizontal.length-1] == b){
                horizontal[horizontal.length] = b;
            }else if(horizontal.length == 0){
                horizontal[0] = b;
            }
            
            // 세로
            if(i == 0){
                vertical[k] = b;
                verticalCount[k] = 1;
            }else if(vertical[k] == b){
                verticalCount[k] = verticalCount[k] + 1;
            }
        }
        
        if(horizontal.length == board.length){
            if(done && (oNum + xNum < totalNum)){
                return 0;
            }
            done = true;
            doneStr = horizontal[0];
        }
    }
    
    var checkDiagonal = diagonal_1[0];
    var doneDiagonal = true;
    for(var i=0; i<diagonal_1.length; i++){
        if(diagonal_1[i] == '.' || checkDiagonal != diagonal_1[i]){
            doneDiagonal = false;
        }
    }
    
    if(doneDiagonal){
        if(done&& (oNum + xNum < totalNum)){
            return 0;
        }
        done = true;
        doneStr = checkDiagonal;
    }
    
    checkDiagonal = diagonal_2[0];
    doneDiagonal = true;
    for(var i=0; i<diagonal_2.length; i++){
        if(diagonal_2[i] == '.' || checkDiagonal != diagonal_2[i]){
            doneDiagonal = false;
        }
    }
    
    if(doneDiagonal){
        if(done&& (oNum + xNum < totalNum)){
            return 0;
        }
        done = true;
        doneStr = checkDiagonal;
    }
    
    for(var i=0; i<vertical.length; i++){
        if(verticalCount[i] == board.length){
            if(done&& (oNum + xNum < totalNum)){
                return 0;
            }
            done = true;
            doneStr = vertical[i];
        }
    }
    
    if(xNum > oNum || oNum > xNum+1){
        return 0;
    }
    
    if(doneStr == 'O' && xNum == oNum){
       return 0; 
    }
    
    if(doneStr == 'X' && xNum != oNum){
        return 0;
    }
    
    return answer;
}


// 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges