package day3;

import java.util.Arrays;
import java.util.Comparator;
import java.io.BufferedWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class cordc{
	int value;
	int rank;
	cordc(int value){
		this.value = value;
	}
}

public class Compression {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		cordc[] cord = new cordc[num];
		cordc[] cord2 = new cordc[num];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<num; i++) {
			cord[i] = new cordc(Integer.parseInt(st.nextToken()));
			cord2[i] = cord[i];
		}
		Arrays.sort(cord, new Comparator<cordc>() {
			@Override
			public int compare(cordc o1, cordc o2) {
				return o1.value-o2.value;
			}
		});
		cord[0].rank = 0;
		for(int i=1; i<num; i++) {
			if(cord[i-1].value==cord[i].value) {
				cord[i].rank = cord[i-1].rank;
			}else {
				cord[i].rank = cord[i-1].rank+1;
			}
		}	
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(cordc c : cord2) {
			bw.write(c.rank + " ");
		}
		bw.close();
	}

}
