package day4;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
public class NQueen {
	// https://www.acmicpc.net/problem/9663
	static boolean[][] chess;
	static int cases;
	static int num;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		num = Integer.parseInt(br.readLine());
		br.close();
		cases=0;
		chess = new boolean[num][num];
		chess(num);
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(String.valueOf(cases));
		bw.close();

	}
	static void chess(int n) {
		if(n==0) {
			cases++;
			return;
		}
		for(int i=0; i<num; i++) {
			if(check(n-1, i)) {
				chess[n-1][i]=true;
				chess(n-1);
				chess[n-1][i]=false;	
			}
		}
	}
	static boolean check(int x, int y) {
		for(int i=x+1; i<num;i++) {
			if(chess[i][y]) {
				return false;
			}
		}
		for(int i=1; x+i<num && y+i<num; i++) {
			if(chess[x+i][y+i]) {
				return false;
			}
		}	
		for(int i=1; x+i<num && y-i>=0; i++) {
			if(chess[x+i][y-i]) {
				return false;
			}
		}
		return true;
	}

}
