package day1;

import java.util.Scanner;
public class BulkRank{
	/* https://www.acmicpc.net/problem/7568
입력      출력 
5        2 2 1 2 5
55 185
58 183
88 186
60 175
46 155 
	 */
	
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        int[][] info = new int[count][2];
        for(int i=0; i<count;i++){
            info[i][0]=sc.nextInt();
            info[i][1]=sc.nextInt();
        }
        int[] rank = new int[count];
        for(int i=0;i<count-1;i++){
            for(int j=i+1;j<count;j++){
                if(info[i][0]>info[j][0]&&info[i][1]>info[j][1]){
                    rank[j]+=1;
                    continue;
                }
                if(info[i][0]<info[j][0]&&info[i][1]<info[j][1]){
                    rank[i]+=1;
                }
            }
        }
        for(int i=0;i<count;i++){
            System.out.print((rank[i]+1) + " ");
        }
    }
 }
