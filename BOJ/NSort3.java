package day2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class NSort3 {
	public static void main(String[] args) throws Exception{
	    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	    int n = Integer.parseInt(reader.readLine());
	    List<Integer> integers = new ArrayList<Integer>();
	    for(int i = 0; i < n; i++) integers.add(Integer.parseInt(reader.readLine()));
	    reader.close();
	    Collections.sort(integers);
	    BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
	    PrintWriter pw = new PrintWriter(writer);
	    for(int i = 0; i < n; i++) pw.println(integers.get(i));
	    pw.flush();
	}
}
