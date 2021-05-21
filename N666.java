package day1;

import java.util.Scanner;

public class N666 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int count=0;
		for(int i=666; i<Integer.MAX_VALUE;i++) {
			if(Integer.toString(i).contains("666")) {
				count+=1;
				if(count==num) { System.out.println(i); break;}
			}
		}
	}
}
