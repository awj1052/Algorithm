package day3;

import java.util.Scanner;
import java.util.ArrayList;

public class StringSort {

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int num = Integer.parseInt(sc.nextLine());
		ArrayList<String> st = new ArrayList<>();
		for(int i=0; i<num; i++) {
			String tmp = sc.nextLine();
			if(!st.contains(tmp)) {
				st.add(tmp);
			}
		}
		st.sort((a,b)->{
			if (a.length()>b.length()) {
				return 1;
			}else if (a.length()<b.length()) {
				return -1;
			}
			for(int i=0; i<a.length();i++) {
				if(a.charAt(i)>b.charAt(i)) {
					return 1;
				}else if (a.charAt(i)<b.charAt(i)) {
					return -1;
				}
			}
			return 0;
		});
		st.forEach(System.out::println);
	}

}