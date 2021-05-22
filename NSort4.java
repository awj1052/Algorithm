package day2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class NSort4 { // https://www.acmicpc.net/problem/10989
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		int[] nums = new int[num];
		int max = Integer.MIN_VALUE;
		for(int i=0; i<num;i++) {
			nums[i]=Integer.parseInt(br.readLine());
			if(max<nums[i]) max=nums[i];
		}
		br.close();
		int[] count = new int[max];
		for(int i : nums) {
			count[i-1]++;			
		}
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i=0; i<max;i++) {
			for(int j=0;j<count[i];j++) {
				bw.write(Integer.toString(i+1));
				bw.newLine();
			}
		}
		bw.flush();
	}
}
