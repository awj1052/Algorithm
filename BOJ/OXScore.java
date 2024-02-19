package day5;

import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class OXScore{
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int i=0; i<num; i++){
            String tmp = sc.nextLine();
            int sum = 0;
            int score = 0;
            for(int j=0; j<tmp.length(); j++){
                if(tmp.charAt(j)=='O'){
                    score++;
                    sum+=score;
                }else{
                    score=0;
                }
            }
            bw.write(String.valueOf(sum));
            bw.newLine();
        }
        bw.close();
    }
}