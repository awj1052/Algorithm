package day4;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Sudoku2 {
	// https://www.acmicpc.net/problem/2239
	static int[][] sudoku;
	static int num0;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sudoku = new int[9][9];
		for(int i=0; i<9; i++) {
			String[] tmp = br.readLine().split("");
			for(int j=0; j<9; j++) {
				sudoku[i][j] = Integer.parseInt(tmp[j]);
				if(sudoku[i][j]==0) {
					num0++;					
				}
			}
		}
		sudoku(0);
	
	}
	static void sudoku(int k) throws Exception {
		if(k==num0) {
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
			for(int[] i : sudoku) {
				for(int j : i) {
					bw.write(String.valueOf(j));
				}
				bw.newLine();
			}
			bw.close();
			System.exit(0);
		}
		for(int i=0; i<9; i++) {
			for(int j=0; j<9; j++) {
				if(sudoku[i][j]==0) {
					for(int n=1; n<=9; n++) {
						if(check(i, j, n)) {
							sudoku[i][j]=n;
							sudoku(k+1);
							sudoku[i][j]=0;	
						}
					}
					return;
				}
			}
		}		
	}
	static boolean check(int i, int j, int n) {
		for(int a=0; a<9; a++) {
			if(sudoku[a][j]==n) {
				return false;
			}
			if(sudoku[i][a]==n) {
				return false;
			}
		}
		for(int a=0; a<3; a++) {
			for(int b=0; b<3; b++) {
				if(sudoku[i/3*3+a][j/3*3+b]==n) {
					return false;
				}				
			}
		}
		return true;
	}

}
