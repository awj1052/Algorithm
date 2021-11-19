package lab09;

import java.io.*;

public class BOJ {

    static String[][] map;
    static int a;
    static int b;
    static int c;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        map = new String[N][N];
        a=0;b=0;c=0;
        for(int i=0; i<N; i++){
            map[i] = br.readLine().split(" ");
        }
        partition(0,0,N);
        System.out.println(a+"\n"+b+"\n"+c);
    }

    static void partition(int y, int x, int size){
        if(check(y,x,size)){
            if(map[y][x].equals("1")){
                c+=1;
            }else if(map[y][x].equals("0")){
                b+=1;
            }else{
                a+=1;
            }
            return;
        }

        size/=3;
        partition(y,x,size);
        partition(y,x+size,size);
        partition(y,x+2*size,size);
        partition(y+size,x,size);
        partition(y+size,x+size,size);
        partition(y+size,x+2*size,size);
        partition(y+2*size,x,size);
        partition(y+2*size,x+size,size);
        partition(y+2*size,x+2*size,size);

    }

    static boolean check(int y, int x, int size){
        for(int i=0; i<size; i++){
            for(int j=0; j<size; j++){
                if(!map[y+i][x+j].equals(map[y][x])){
                    return false;
                }
            }
        }
        return true;
    }
}