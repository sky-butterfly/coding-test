package programmers.level1;

public class Test1 {
    public String solution(String s) {
        String answer = "";
        StringBuffer sb = new StringBuffer();        
        
        s = s.toLowerCase();
        int index = 0;
        for(int i=0; i<s.length(); i++){
            
            String ss = s.substring(i, i+1);
            
            if(ss.equals(" ")){
                sb.append(" ");
                index = 0;
                continue;
            }
            
            if(index == 0 || (index%2) == 0){
                ss = ss.toUpperCase();
            }
            
            sb.append(ss);
            index++;
        }        
        
        answer = sb.toString();
        
        return answer;
    }
}
