package programmers.level2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Test2 {
	public String[] solution(String[] record) {
        String[] answer = {};
        
        List<String> list = new ArrayList<>();
        Map<String, String> map = new HashMap<>();

        for(String r : record){
            String[] arr = r.split(" ");
                                   
            if(!map.containsKey(arr[1])){
                map.put(arr[1], arr[2]);
            }                    
            
            switch(arr[0]){
                case "Enter" :                    
                    map.put(arr[1], arr[2]);
                    list.add(arr[1]+" 들어왔습니다.");
                    break;
                case "Leave" :
                    list.add(arr[1]+" 나갔습니다.");
                    break;
                case "Change" :
                    map.put(arr[1], arr[2]);
                    break;
            }
        }
        
        answer = new String[list.size()];
        for(int i=0; i<list.size(); i++){
            
            String l = list.get(i);
            String[] arr = l.split(" ");
            String id = arr[0];
            String name = map.get(id);
            
            l = name + "님이 "+arr[1];
            answer[i] = l;
        }
        
        return answer;
    }
}
