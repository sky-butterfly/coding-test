package 프로그래머스.Level_0.java;

import java.util.*;

class Solution {
    public int solution(int[] array, int n) {
        int answer = array[0];
        
        Arrays.sort(array);
        
        int abs = Math.abs(n-array[0]);
        int num = abs;
        
        for(int i=1; i<array.length; i++){
            int a = array[i];
            
            abs = Math.abs(n-a);
            
            if(abs < num){
                num = abs;
                answer = a;
            }
        }
        
        return answer;
    }
}
