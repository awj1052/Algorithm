package chap06;

public class SelfNum {
	// https://www.acmicpc.net/problem/4673
	static boolean[] arr;
	public static void main(String[] args) {
		arr = new boolean[10001];
		for(int i=1; i<=10000; i++) {
			if(!arr[i]) {
				self(i);
				System.out.println(i);
			}
		}
	}
	static void self(int a) {
		int sum=0;
		sum+=a;
		while(a>0) {
			sum+=a%10;
			a/=10;
		}
		if(sum>10000) {
			return;
		}
		arr[sum]=true;
		self(sum);
	}
}
