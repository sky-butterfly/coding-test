package 프로그래머스.Level_0.java;

import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> list = new ArrayList<>();
        
        int i = 0;
        
        for(String str : intStrs){
            str = str.substring(s, s+l);
            i = Integer.parseInt(str);
            if(i > k){
                list.add(i);
            }
        }        
        
        int[] answer = new int[list.size()];
        for(int n = 0; n<list.size(); n++){
            answer[n] = list.get(n);
        }
        
        return answer;
    }
}
