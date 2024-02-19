package chap14;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Operator {
	static int max, min, N;
	static int[] input;
	static int[] num;
	static int[] oper;
	public static void main(String[] args) throws Exception{
		max = Integer.MIN_VALUE;
		min = Integer.MAX_VALUE;
		input = new int[4];
		oper = new int[4];
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		num = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			num[i]=Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<4; i++) {
			input[i]=Integer.parseInt(st.nextToken());
		}
		br.close();
		a(1, num[0]);
		System.out.println(max);
		System.out.println(min);
	}
	
	static void a(int count, int cost) {
		if(count==N) {
			if(cost>max) {
				max=cost;
			}
			if (cost<min) {
				min=cost;
			}
			return;
		}
		if (oper[0]<input[0]) {
			oper[0]+=1;
			a(count+1, cost+num[count]);
			oper[0]-=1;
		}
		if (oper[1]<input[1]) {
			oper[1]+=1;
			a(count+1, cost-num[count]);
			oper[1]-=1;
		}
		if (oper[2]<input[2]) {
			oper[2]+=1;
			a(count+1, cost*num[count]);
			oper[2]-=1;
		}
		if (oper[3]<input[3]) {
			oper[3]+=1;
			a(count+1, cost/num[count]);
			oper[3]-=1;
		}
	}

}
