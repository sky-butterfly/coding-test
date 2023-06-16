package 프로그래머스.Level_0.java;

class Solution {
    public int solution(int n) {
        int answer = 1;
        
        int i=1;
        while(true){
            answer *= i;
            if(answer == n){
                answer = i;
                break;
            }
            if(answer > n){
                answer = i-1;
                break;
            }
            i++;
        }
        
        return answer;
    }
}
