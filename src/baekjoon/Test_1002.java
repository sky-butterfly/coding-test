package baekjoon;

import java.util.Scanner;

public class Test_1002 {

	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		int x1, y1, r1, x2, y2, r2, count;
		count = sc.nextInt();
		
		for(int i=0; i<count; i++) {
			x1 = sc.nextInt();
			y1 = sc.nextInt();
			r1 = sc.nextInt();
			x2 = sc.nextInt();
			y2 = sc.nextInt();
			r2 = sc.nextInt();
			
			if(x1 == x2 && y1 == y2 && r1 == r2) {
				System.out.println(-1);
				continue;
			}
			int r = (int) (Math.pow((x2-x1), 2) + Math.pow((y2-y1), 2));
			
			if( r > Math.pow((r1+r2), 2)) {
				System.out.println(0);
				continue;
			}
			
			if((r2 != r1) && r < Math.pow((r2-r1), 2)) {
				System.out.println(0);
				continue;
			}
			
			if(r == Math.pow((r2-r1), 2)) {
				System.out.println(1);
				continue;
			}
			
			if(r == Math.pow((r2+r1), 2)) {
				System.out.println(1);
				continue;
			}
			System.out.println(2);
		}
	}

}
