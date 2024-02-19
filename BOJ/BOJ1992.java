package lab09;

import java.io.*;

public class BOJ {

    static String[][] map;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        map=new String[N][N];
        for(int i=0; i<N; i++){
            map[i]=br.readLine().split("");
        }
        partition(0,0,N);

    }

    static void partition(int y, int x, int size){
        if(check(y,x,size)){
            if(map[y][x].equals("0")){
                System.out.print(0);
            }else{
                System.out.print(1);
            }
            return;
        }
        size/=2;
        System.out.print("(");
        partition(y,x,size);
        partition(y,x+size,size);
        partition(y+size,x,size);
        partition(y+size,x+size,size);
        System.out.print(")");
    }

    static boolean check(int y, int x, int size){
        for(int i=0; i<size; i++){
            for(int j=0; j<size; j++){
                if(!map[i+y][j+x].equals(map[y][x])){
                    return false;
                }
            }
        }
        return true;
    }
}