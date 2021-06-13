package chap06;

import java.util.Scanner;

public class Sequence {
	// https://www.acmicpc.net/problem/1065
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int input = sc.nextInt();
		if(input<100) {
			System.out.println(input);
			return;
		}
		int count = 0;
		loop : for(int i=110; i<=input;i++) {
			int a = i;
			int b = a%10;
			a/=10;
			int c = a%10;
			a/=10;
			while(a>0) {
				int d = a%10; 
				if(d-c!=c-b) {
					continue loop;
				}
				a/=10;
			}
			count++;
		}
		System.out.println(count+99);
	}	
}
