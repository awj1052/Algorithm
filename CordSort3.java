package day3;

import java.util.Scanner;
import java.util.ArrayList;

class cord{
	int x;
	int y;
	cord(int x, int y){
		this.x=x;
		this.y=y;
	}
}

public class CordSort3 {

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		ArrayList<cord> cords = new ArrayList<>();
		for(int i=0; i<num; i++) {
			cords.add(new cord(sc.nextInt(), sc.nextInt()));
		}
		cords.sort((a,b)->{
			if(a.y > b.y) {
				return 1;
			}else if (a.y < b.y) {
				return -1;
			}
			if (a.x > b.x) {
				return 1;
			}else if (a.x < b.x) {
				return -1;
			}
			return 0;
		});
		cords.forEach(c->System.out.println(c.x + " " + c.y));
	}

}