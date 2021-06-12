package chap06;

public class SumN {
	// https://www.acmicpc.net/problem/15596
	long sum(int[] a) {
		long sum=0;
		for(int i : a) {
			sum+=i;
		}
		return sum;
	}
}
