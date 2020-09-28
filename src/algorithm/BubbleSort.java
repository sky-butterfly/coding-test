package algorithm;

public class BubbleSort {

	public static void main(String[] args) {
		
		int[] arr = {5, 1, 80, 100, 4, 2, 3, 90, 7, 6};
		int size = arr.length;
		
		for(int i=0; i<size; i++) {
			
			for(int k=0; k<size-i-1; k++) {
				
				if(arr[k+1] >= arr[k]) {
					continue;				
				}
				
				int tmp = arr[k+1];
				arr[k+1] = arr[k];
				arr[k] = tmp;
			}
		}

		for(int a : arr) {
			System.out.println(a);
		}
	}

}
