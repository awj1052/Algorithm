package day3;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class member{
	int age;
	String name;
	member(int age, String name){
		this.age = age;
		this.name = name;
	}
	public String toString() {
		return age + " " + name;
	}
}

public class memberSort {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = Integer.parseInt(sc.nextLine());
		member[] arr = new member[num];
		for(int i=0; i<num;i++) {
			String[] tmp = sc.nextLine().split(" ");
			arr[i]=new member(Integer.parseInt(tmp[0]), tmp[1]);
		}
		Arrays.sort(arr, new Comparator<member>() {

			@Override
			public int compare(member o1, member o2) {
				return o1.age - o2.age;
			}
			
		});
		for(member m : arr) {
			System.out.println(m);
		}

	}

}
