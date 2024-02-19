package day5;

import java.util.Scanner;

public class Num{
	// https://www.acmicpc.net/problem/2577
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int[] count = new int[10];
        String tmp = String.valueOf(a*b*c);
        for(int i=0; i<tmp.length();i++)
            count[Integer.parseInt(tmp.charAt(i)+"")]++;
        for(int i : count)
            System.out.println(i);
   }
}
