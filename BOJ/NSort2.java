package day2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class NSort2 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		int[] nums = new int[num];
		for(int i=0;i<num;i++) nums[i]=Integer.parseInt(br.readLine());
		br.close();
		Arrays.sort(nums);
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i : nums) {
			bw.write(Integer.toString(i)); 
			bw.newLine();
		}
		bw.flush();
	}
}
