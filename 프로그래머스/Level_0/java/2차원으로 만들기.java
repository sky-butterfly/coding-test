package 프로그래머스.Level_0.java;

class Solution {
    public int[][] solution(int[] num_list, int n) {
        
        if(num_list.length < 1){
            return new int[0][0];
        }
        
        int[][] answer = new int[num_list.length/n][n];
        
        int size = num_list.length/n;
        for(int i=0; i<size; i++){
            for(int j=0; j<n; j++){
                
                answer[i][j] = num_list[(i*n)+j];
            }
        }
        
        return answer;
    }
}