package day5;

import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.text.DecimalFormat;

public class OverAverage {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		DecimalFormat df = new DecimalFormat("0.000");
		int num = sc.nextInt();
		int[] arr;
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i=0;i<num;i++) {
			int p = sc.nextInt();
			int sum = 0;
			arr = new int[p];
			for(int j=0; j<p; j++) {
				arr[j]=sc.nextInt();
				sum+=arr[j];
			}
			sum=(int) Math.ceil(sum/p);
			int count = 0;
			for(int j=0; j<p; j++) {
				if(arr[j]>sum) {
					count++;
				}
			}
			bw.write(df.format((Math.round(100000.0*count/p)/1000.0))+ "%");
			bw.newLine();
			
		}
		bw.close();

	}

}
