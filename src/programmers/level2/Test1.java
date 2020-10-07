package programmers.level2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Test1 {
	public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        
        List<String> list = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        
        String str = words[0].substring(0,1);
        int index = 1;
        for(String w : words){            
            
            if(!map.containsKey(index)){
                map.put(index, 0);
            }
            
            map.put(index, map.get(index)+1);

            if(!str.equals(w.substring(0,1))){
                answer[0] = index;
                answer[1] = map.get(index);
                break;
            }
            
            str = w.substring(w.length()-1);
            
            if(list.contains(w)){
                answer[0] = index;
                answer[1] = map.get(index);
                break;
            }
            
            if(w.length() < 2){
                answer[0] = index;
                answer[1] = map.get(index);
                break;
            }
                      
            list.add(w);
            
            if(index == n){
                index = 1;    
            }else{
                index++;
            }
        }

        return answer;
    }
}
