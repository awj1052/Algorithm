package lab09;

// BOJ 2636

// 치즈가 그저 빈 공간과 닿아있으면 없어지는 것으로 착각했다.
// 바깥과 연결된 공간만 치즈를 없앨 수 있도록 바깥과 안의 빈 공간을 구분한다.

import java.io.*;
import java.util.*;

public class BOJ {

    static int[][] map;
    static int[] dy = {1,-1,0,0};
    static int[] dx = {0,0,1,-1};
    static int N,M;
    static int time, cheeze;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = br.readLine().split(" ");
        N = Integer.parseInt(tmp[0]); M = Integer.parseInt(tmp[1]);
        map = new int[N][M];
        cheeze=0; time=1;
        for(int i=0; i<N; i++) {
            tmp = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                if (tmp[j].equals("1")) {
                    map[i][j] = 1;
                    cheeze += 1;
                }
            }
        }
        int r;
        while((r=bfs())==-1){
            time+=1;
        }
        System.out.println(time+"\n"+r);
    }

    static int bfs() {
        // 외부 빈 공간 구분
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visit = new boolean[N][M];
        q.offer(new int[]{0,0}); // 무조건 외부 빈 공간 (문제 조건)
        while(!q.isEmpty()){
            int[] tmp = q.poll();
            int y = tmp[0];
            int x = tmp[1];
            for(int i=0; i<4; i++){
                int ny = y + dy[i];
                int nx = x + dx[i];
                if(Range(ny,nx) && !visit[ny][nx] && map[ny][nx] != 1){
                    map[ny][nx]=-1;
                    visit[ny][nx]=true;
                    q.offer(new int[]{ny,nx});

                }
            }
        }

        // 외부 빈 공간과 닿은 치즈를 내부 빈 공간 취급
        int c=0;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++){
                if(map[y][x]!=1) continue;
                for (int i = 0; i < 4; i++) {
                    int ny = y + dy[i];
                    int nx = x + dx[i];
                    if(Range(ny, nx) && map[ny][nx]==-1) {
                        map[y][x]=0;
                        c+=1;
                        break;
                    }
                }
            }
        }
        cheeze-=c;
        if(cheeze==0) {
            return c;
        }
        return -1;

    }

    static boolean Range(int y, int x){
        return 0 <= y && y < N && 0 <= x && x < M;
    }
}