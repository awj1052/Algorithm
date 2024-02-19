package day1;

import java.util.Scanner;
public class NConstructor{ // 256(=245+2+4+5) 245의 분해합은 256. 256의 생성자는 245
	                       // 자연수 N 입력시 생성자를 출력함
	                       // https://www.acmicpc.net/problem/2231
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        int value = (int)(Math.log10(input)+1);
        int output = 0;
        for(int i=input-9*value;i<input;i++){
            int sum = i;
            int num = i;
            while(num!=0){
                sum+=num%10;
                num/=10;
            }
            if(input==sum){ output=i; break; }
        }
        System.out.print(output);
    }
}
