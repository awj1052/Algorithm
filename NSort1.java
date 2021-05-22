package day2;

import java.util.Scanner;

public class NSort1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[] nums = new int[num];
		for(int i=0; i<num;i++){
			nums[i]=sc.nextInt();
		}
		for(int i=0; i<num-1;i++) {
			boolean changed = false;
			for(int j=0;j<num-1-i;j++) {
				if(nums[j]>nums[j+1]) {
					int tmp = nums[j];
					nums[j]=nums[j+1];
					nums[j+1]=tmp;
					changed = true;
				}
			}
			if(!changed) { break; }
		}
		for(int i : nums) {
			System.out.println(i);
		}
	}
}
