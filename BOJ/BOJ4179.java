package lab09;

// BOJ 4179
// 컴파일 에러 -> switch case 을 lambda-like syntax 로 사용했는데
// 찾아보니 이는 Java 14부터 가능한 기능이였다고 함. Java 11에서는 컴파일 에러 나는 것이 당연.
// BFS를 도는데 J가 먼저 움직이고 F를 움직일 수 있도록 했더니 틀렸다.
// 순서를 바꿔 F를 먼저, J가 나중에 움직일 수 있도록 바꾸었더니 정답처리 됐다.
// Python이 편해서 자주 하다보니 제출할 때 클래스 이름을 바꾸지 않아 컴파일 에러를 계속 내버렸다.

import java.io.*;
import java.util.*;

public class BOJ {

    static final int[] dx = {0,0,-1,1};
    static final int[] dy = {1,-1,0,0};
    static int[][] map;
    static int R;
    static int C;
    static Queue<int[]> q;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp;
        tmp = br.readLine().split(" ");
        R = Integer.parseInt(tmp[0]);
        C = Integer.parseInt(tmp[1]);
        map = new int[R][C];
        q = new LinkedList<>();
        int a=0,b=0;
        for(int i=0; i<R; i++){
            tmp = br.readLine().split("");
            for(int j=0; j<C; j++){
                if(tmp[j].equals("F")){
                    q.offer(new int[]{i, j});
                    map[i][j] = -1;
                }else if(tmp[j].equals("J")){
                    map[i][j] = 1;
                    a=i; b=j;
                }else if(tmp[j].equals(".")){
                    map[i][j] = 0;
                }else {
                    map[i][j] = -1;
                }
            }
        }
        if(a==0 || a==R-1 || b==0 || b==C-1){ System.out.println(1); return;}
        q.offer(new int[]{a,b});
        //bfs(a,b);
        bfs_main();
    }

    static boolean inRange(int y, int x){
        return 0 <= y && y < R && 0 <= x && x < C;
    }

    static void bfs_main(){
        while(!q.isEmpty()){
            int[] tmp = q.poll();
            int y = tmp[0];
            int x = tmp[1];
            if(map[y][x]!=-1 && (y==0 || y==R-1 || x==0 || x==C-1)){
                System.out.println(map[y][x]);
                return;
            }
            bfs(y,x);
        }
        System.out.println("IMPOSSIBLE");
    }

    static void bfs(int y, int x){
        for(int i=0; i<4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(inRange(ny, nx) && map[ny][nx]==0){
                q.offer(new int[]{ny,nx});
                if(map[y][x]==-1) {
                    map[ny][nx] = -1;
                }else{
                    map[ny][nx] = map[y][x] + 1;
                }
            }
        }
    }
}