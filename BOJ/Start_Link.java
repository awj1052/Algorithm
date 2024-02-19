package chap14;

import java.util.Scanner;
import java.util.StringTokenizer;

public class Start_Link {
	// https://www.acmicpc.net/problem/14889
	static int stat[][];
	static boolean pick[];
	static int min, N;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = Integer.parseInt(sc.nextLine());
		stat = new int[N][N];
		pick = new boolean[N];
		min=Integer.MAX_VALUE;
		for(int i=0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(sc.nextLine());
			for(int j=0; j<N; j++) {
				stat[i][j]=Integer.parseInt(st.nextToken());
			}
		}
		sc.close();
		a(0, 0);
		System.out.println(min);
	
	}
	
	static void a(int picked, int n) {
		if (n==N/2) {
			int[] S = new int[N/2];
			int[] L = new int[N/2];
			int s = 0, l = 0;
			for(int i=0; i<N; i++) {
				if(pick[i]){
					S[s]=i;
					s+=1;
				}else {
					L[l]=i;
					l+=1;
				}
					
			}
			s = 0; l = 0;
			for(int i=0; i<N/2-1; i++) {
				for(int j=i+1; j<N/2; j++) {
					s+= stat[S[i]][S[j]] + stat[S[j]][S[i]];
					l+= stat[L[i]][L[j]] + stat[L[j]][L[i]];
				}
			}
			if (s-l > 0) {
				if (min > s-l) {
					min=s-l;
				}
			}else {
				if (min > l-s) {
					min=l-s;
				}
			}
					
			return;
		}
		
		if (min == 0) {
			return;
		}
		int tmp = N/2 + n;
		for(int i=picked+1; i<=tmp; i++) {
			pick[i]=true;
			a(i, n+1);
			pick[i]=false;
		}
	}

}