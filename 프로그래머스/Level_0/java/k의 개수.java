package 프로그래머스.Level_0.java;

class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String strK = String.valueOf(k);
        
        for(int n=i; n<j+1; n++){
            String str = String.valueOf(n);
            int m = str.length() - str.replace(strK, "").length();
            if(m > 0){
                answer += m;
            }
        }
        
        return answer;
    }
}