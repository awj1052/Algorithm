package day5;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class NewAverage {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int sub = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] grade = new int[sub];
		int max = Integer.MIN_VALUE;
		for(int i=0; i<sub; i++) {
			grade[i] = Integer.parseInt(st.nextToken());
			if(max<grade[i]) {
				max=grade[i];
			}
		}
		double sum = 0;
		for(int i=0; i<sub; i++) {
			sum+=100.0*grade[i]/max;
		}
		System.out.println(sum/sub);
		

	}

}
