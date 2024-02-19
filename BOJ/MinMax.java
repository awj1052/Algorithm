package day5;

import java.util.Scanner;
public class MinMax {
	// https://www.acmicpc.net/problem/10818
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for(int i=0;i<num;i++){
            int tmp = sc.nextInt();
            if(tmp>max){
                max=tmp;
            }
            if(tmp<min){
                min=tmp;
            }
        }
        System.out.println(min + " " + max);
    }
}
