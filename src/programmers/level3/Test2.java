package programmers.level3;

public class Test2 {
	public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] check = new boolean[n];
        
        for(int i=0; i<n; i++){
            if(!check[i]){
                answer++;
                dfs(check, computers, i);
            }
        }
        
        return answer;
    }
    
    public void dfs(boolean[] check, int[][] computers, int i){       
        check[i] = true;
        for(int k=0; k<computers.length; k++){
            if(!check[k] && computers[i][k] == 1){
                dfs(check, computers, k);
            }
        }
    }
}
