package day4;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class NM {
	static boolean[] check;
	static int N;
	static int M;
	static int[] visit;
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		check = new boolean[N]; // 배열의 크기가 N+1 이고
		visit = new int[N]; //
		m(0);
		bw.close();
	}
	static void m(int n) throws Exception {
		if(n==M) { //
			for(int i=0; i<M; i++) { // 1부터 시작한다면
				bw.write((visit[i]+1) + " "); // +1을 안해도 됨
			}
			bw.newLine();
			return;
		}
		for(int i=0; i<N; i++) { //
			if(!check[i]) {
				check[i]=true;
				visit[n]=i;
				m(n+1);
				check[i]=false;
			}
		}
	}
}
