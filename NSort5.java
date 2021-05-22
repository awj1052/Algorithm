package day2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class NSort5 { // https://www.acmicpc.net/problem/10989
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		int[] count = new int[10001];
		for(int i=0; i<num;i++) {
			count[Integer.parseInt(br.readLine())]++;
		}
		br.close();
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i=1; i<10001;i++) {
			for(int j=0;j<count[i];j++) {
				bw.write(Integer.toString(i));
				bw.newLine();
			}
		}
		bw.flush();
	}
}
