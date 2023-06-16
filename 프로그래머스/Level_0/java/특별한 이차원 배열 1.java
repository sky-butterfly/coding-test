package 프로그래머스.Level_0.java;

class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                
                if(i==j){
                    answer[i][j] = 1;
                    continue;
                }
                answer[i][j] = 0;
            }
        }        
        
        return answer;
    }
}
