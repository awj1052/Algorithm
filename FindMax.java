package day5;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class FindMax{
	// https://www.acmicpc.net/problem/2562
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int max = Integer.parseInt(br.readLine());
        int idx = 1;
        for(int i=0; i<8;i++){
            int tmp = Integer.parseInt(br.readLine());
            if(tmp>max){
                max=tmp;
                idx=i+2;
            }
        }
        br.close();
        System.out.println(max);
        System.out.println(idx);
    }
}