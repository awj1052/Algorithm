package week11;

import java.util.Scanner;

public class OperTypeCheck {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		while(!str.contains("E") && !str.contains("e")) {
			str+=sc.nextLine();
		}
		while(str.contains("R")) {
			str=str.substring(str.indexOf('R')+1);
		}
		while(str.contains("r")) {
			str=str.substring(str.indexOf('r')+1);
		}
		char[] arr = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
		int[] count = new int[10];
		char[] arr2 = {'+', '-', '/', '*', '%'};
		int[] count2 = new int[5];
		char[] array = new char[str.length()];
		loop : for(int i=0; i<str.length();i++) {
			if(str.charAt(i)=='E' || str.charAt(i)=='e') {
				break;
			}
			for(int j=0;j<10;j++) {
				if(str.charAt(i)==arr[j]) {
					count[j]++;
					continue loop;
				}
			}
			for(int j=0; j<5; j++) {
				if(str.charAt(i)==arr2[j]) {
					count2[j]++;
					continue loop;
				}
			}
		}
		int idx=0;
		int idx1=0;
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		for(int i=0; i<10;i++) {
			if(max<count[9-i]) {
				max=count[9-i];
				idx=9-i;
			}
			/*
			if(min>count[9-i] && count[9-i]>0) {
				min=count[9-i];
				idx1=9-i;
			}
			*/
			if(min>count[i] && count[i]==0) {
				min=count[i];
				idx1=i;
			}
		}
		int idx2=0;
		int max2 = count2[0];
		for(int i=1; i<5;i++) {
			if(max2<count2[i]) {
				max2=count2[i];
				idx2=i;
			}
		}
		System.out.print(arr[idx]);
		System.out.print(arr2[idx2]);
		System.out.print(arr[idx1] + "=");
		if(idx2==0) {
			System.out.print((int)(arr[idx]-'0') + (int)(arr[idx1]-'0'));
		}else if(idx2==1) {
			System.out.print((int)(arr[idx]-'0') - (int)(arr[idx1]-'0'));
		}else if(idx2==2) {
			System.out.print((int)(arr[idx]-'0') / (int)(arr[idx1]-'0'));
		}else if(idx2==3) {
			System.out.print((int)(arr[idx]-'0') * (int)(arr[idx1]-'0'));
		}else if(idx2==4) {
			System.out.print((int)(arr[idx]-'0') % (int)(arr[idx1]-'0'));
		}
	}
}
