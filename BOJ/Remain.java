package day5;

import java.util.Scanner;

public class Remain{
	// https://www.acmicpc.net/problem/3052
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        boolean[] remain = new boolean[42];
        int count = 0;
        for(int i=0; i<10; i++) {
        	int tmp = sc.nextInt();
        	if(!remain[tmp%42]) {
        		remain[tmp%42]=true;
        		count++;
        	}
        }
        System.out.println(count);
   }
}