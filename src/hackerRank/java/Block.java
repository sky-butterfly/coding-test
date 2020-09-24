package hackerRank.java;

import java.util.Scanner;

@SuppressWarnings("resource")
public class Block {

	static boolean flag = true;
	static int B = 1;
	static int H = 1;

	static {
		Scanner sc = new Scanner(System.in);
		B = sc.nextInt();
		H = sc.nextInt();

		if (B <= 0 || H <= 0) {
			flag = false;
			System.out.println("java.lang.Exception: Breadth and height must be positive");
		}
	}

	public static void main(String[] args) {
		if (flag) {
			int area = B * H;
			System.out.print(area);
		}

	}

}
