// BOJ 3190

import java.io.*;
import java.util.*;

public class BOJ {
    public static void main(String[] args) throws IOException {
        final int[] dx = {1, 0, -1, 0};
        final int[] dy = {0, -1, 0, 1};
        int dir = 0; // 뱀의 방향 : dx, dy의 index가 되는 변수 0<=dir<4

        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] map = new int[N][N];
        int K = Integer.parseInt(br.readLine());
        while(K-->0){
            String[] tmp = br.readLine().split(" ");
            map[Integer.parseInt(tmp[0])-1][Integer.parseInt(tmp[1])-1] = 1;
        }
        LinkedList<int[]> cmd = new LinkedList<>();
        int L = Integer.parseInt(br.readLine());
        while(L-->0){
            String[] tmp = br.readLine().split(" ");
            if(tmp[1].equals("L")){
                cmd.add(new int[]{Integer.parseInt(tmp[0]), 1});
            }else{ // D (RIGHT)
                cmd.add(new int[]{Integer.parseInt(tmp[0]), -1});
            }
        }
        br.close();

        int time = 0;
        int y=0; int x=0; map[0][0]=2; // 뱀 위치 표시
        Queue<int[]> snake = new LinkedList<>();
        snake.add(new int[]{0,0});

        while(true){
            time+=1;
            y+=dy[dir]; x+=dx[dir];
            if(x<0 || x>=N || y<0 || y>=N || map[y][x]==2) break; // 부딫혀서 끝
            if(map[y][x]!=1){
                int[] tmp = snake.poll();
                map[tmp[0]][tmp[1]] = 0;
            }
            snake.add(new int[]{y,x}); map[y][x]=2;
            if(cmd.size() > 0 && cmd.get(0)[0] == time) {
                dir += cmd.get(0)[1];
                dir%=4;
                if(dir<0) dir+=4;
                cmd.remove(0);
            }
        }
        System.out.println(time);
    }
}
