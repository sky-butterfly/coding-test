package hackerRank.java;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Calendar;

public class DateTime {

	public static void main(String[] args) {
		System.out.println(findDay(2, 13, 2010));
	}
	
	public static String findDay(int month, int day, int year) {
		
		String result = "";

        Calendar cal = Calendar.getInstance();
        cal.set(year, month-1, day);
        
        int week = cal.get(Calendar.DAY_OF_WEEK);
        
        switch(week){
            case 2:
                result = "MONDAY";
                break;
            case 3:
                result = "TUESDAY";
                break;
            case 4:
                result = "WEDNESDAY";
                break;
            case 5:
                result = "THURSDAY";
                break;
            case 6:
                result = "FRIDAY";
                break;
            case 7:
                result = "SATURDAY";
                break;
            case 1:
                result = "SUNDAY";
                break;
        }

        return result;
	}

}

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int month = Integer.parseInt(firstMultipleInput[0]);

        int day = Integer.parseInt(firstMultipleInput[1]);

        int year = Integer.parseInt(firstMultipleInput[2]);

        String res = DateTime.findDay(month, day, year);

        bufferedWriter.write(res);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}