package day1;

import java.util.Scanner;
public class ChessPaint { // https://www.acmicpc.net/problem/1018
	/*
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

12
	 */

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] line1 = sc.nextLine().split(" ");
		int height = Integer.parseInt(line1[0]);
		int width = Integer.parseInt(line1[1]);
		boolean[][] chess = new boolean[width][height];
		for(int i=0; i<height;i++) {
			String line = sc.nextLine();
			for(int j=0;j<width;j++) {
				if(line.charAt(j)=='W') {
					chess[j][i]=true;
				}
			}
		}
		int cost = 0;
		boolean check;
		int min = Integer.MAX_VALUE;
		for(int i=0; i<width-7;i++) {
			for(int j=0; j<height-7;j++) {
				cost=0;
				check = false; // B
				loop : for(int m=0; m<8;m++) {
					for(int n=0; n<8;n++) {
						if(chess[i+n][j+m]!=check) {
							cost+=1;
							if(cost>=min) { break loop;}
						}
						check=!check;
					}
					check=!check;
				}
				if(cost<min) { min=cost;}
				cost=0;
				check = true; // W
				loop : for(int m=0; m<8;m++) {
					for(int n=0; n<8;n++) {
						if(chess[i+m][j+n]!=check) {
							cost+=1;
							if(cost>=min) { break loop;}
						}
						check=!check;
					}
					check=!check;
				}
				if(cost<min) { min=cost;}
			}
		}
		System.out.println(min);

	}

}