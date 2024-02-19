package day3;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class CordSort {

	public static void main(String[] args){
		ArrayList<Integer> num = new ArrayList<>();
		ArrayList<Integer> num2 = new ArrayList<>();
		ArrayList<Integer> num3 = new ArrayList<>();
		int count = 0;
		String[] input;
		try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in));){
            count = Integer.parseInt(br.readLine());
            for(int i=0; i<count; i++){    	
            	input = br.readLine().split(" ");
                num.add(Integer.parseInt(input[0]));
                num2.add(Integer.parseInt(input[1]));
                num3.add(i);
            }
		}catch(Exception e) {
			e.printStackTrace();
		}
		num3.sort((a,b)->{
			if(num.get(a)>num.get(b)) {
				return 1;
			}else if(num.get(a)<num.get(b)) {
				return -1;
			}
			if(num2.get(a)>num2.get(b)) {
				return 1;
			}else if(num2.get(a)<num2.get(b)) {
				return -1;
			}
			return 0;
		});
		try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));){
            for(int i : num3){
                bw.write(num.get(i) + " " + num2.get(i)+"\n");
            }
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}