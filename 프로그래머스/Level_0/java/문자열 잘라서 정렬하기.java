package 프로그래머스.Level_0.java;

import java.util.*;

class Solution {
    public String[] solution(String myString) {
        String[] answer = myString.split("x");
        
        Arrays.sort(answer);
        
        List<String> strArr = new ArrayList<>(Arrays.asList(answer));
        strArr.removeAll(Arrays.asList("", null));
        
        answer = strArr.toArray(new String[strArr.size()]);
        
        return answer;
    }
}