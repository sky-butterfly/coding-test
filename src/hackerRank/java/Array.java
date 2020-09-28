package hackerRank.java;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Array {
	
	 // Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr) {
    	
    	List<Integer> list = new ArrayList<Integer>();
        int sum = 0;

        for(int i=0; i<arr.length; i++){

            if(arr.length-1 < i+2){
                break;
            }

            for(int k=0; k<arr.length; k++){
                sum = 0;

                if(arr.length-1 < k+2){
                    break;
                }               

                sum += arr[i][k];
                sum += arr[i][k+1];
                sum += arr[i][k+2];
                sum += arr[i+1][k+1];
                sum += arr[i+2][k];
                sum += arr[i+2][k+1];
                sum += arr[i+2][k+2];

                list.add(sum);
            }
        }

        Collections.sort(list);

        return list.get(list.size()-1);
    }

	private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        int result = hourglassSum(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
