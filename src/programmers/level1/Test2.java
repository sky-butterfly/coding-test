package programmers.level1;

import java.util.Stack;

public class Test2 {

	public int solution(int[][] board, int[] moves) {
        int answer = 0;
        
        Stack<Integer> stack = new Stack<Integer>();
            
        for(int m : moves){     
            
            int num = 0;
            
            for(int i=0; i<board.length; i++){
                
                num = board[i][m-1];
                
                if(num == 0){
                    continue;
                }
                
                board[i][m-1] = 0;
                
                break;
            }
            
            if(num == 0){
                continue;
            }
            
            if(stack.size() == 0){
                stack.push(num);
                continue;
            }else if(stack.peek() == num){
                stack.pop();
                answer = answer + 2;
            }else{
                stack.push(num);
            }
        }
        
        return answer;
    }
}