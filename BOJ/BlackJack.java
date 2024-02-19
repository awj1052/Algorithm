package day1;

import java.util.Scanner;

public class BlackJack { // https://www.acmicpc.net/problem/2798
                         // 예제 입력     예제 출력  
	                     // 5 21       21
	                     // 5 6 7 8 9
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cards = sc.nextInt();
		int max = sc.nextInt();
		int[] card = new int[cards];
		for(int i=0; i<cards;i++) {
			card[i] = sc.nextInt();
		}
		int output = 0;
		for(int i=0; i<cards-2;i++) {
			for(int j=i+1;j<cards-1;j++) {
				for(int k=j+1;k<cards;k++) {
					if(card[i]+card[j]+card[k]>output&&card[i]+card[j]+card[k]<=max) {
						output=card[i]+card[j]+card[k];
					}
				}
			}
		}
		System.out.println(output);
	}

}
