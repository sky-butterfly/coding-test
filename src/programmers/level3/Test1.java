package programmers.level3;

import java.util.Arrays;

public class Test1 {
	public int solution(int[] A, int[] B) {
        int answer = 0;
        
        Arrays.sort(A);
        Arrays.sort(B);
        
        int a = 0;
        int b = 0;
        for(int i=0; i<A.length; i++){
            if(A[a] > B[b]){
                b++;
                continue;
            }
            
            if(A[a] == B[b]){
                b++;
                continue;
            }
            
            a++;
            b++;
            
            answer++;
        }        
        
        return answer;
    }
}
