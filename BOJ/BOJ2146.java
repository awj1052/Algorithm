package lab09;

// BOJ 2146

import java.io.*;
import java.util.*;

public class BOJ {

    static final int[] dx = {0,0,1,-1};
    static final int[] dy = {1,-1,0,0};
    static int[][] map;
    static int N;
    static int cnt;
    static int min = Integer.MAX_VALUE;
    static int[][] visit;
    static Queue<int[]> q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map= new int[N][N];
        for(int i=0; i<N; i++){
            String[] tmp = br.readLine().split(" ");
            for(int j=0; j<N; j++){
                map[i][j]=Integer.parseInt(tmp[j]);
            }
        }

        // DFS + BFS
        cnt=1;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(map[i][j]==1){
                    cnt+=1;
                    q = new LinkedList<>();
                    visit = new int[N][N];
                    dfs(i,j);
                    bfs();
                }
            }
        }
        System.out.println(min);
    }

    static boolean inRange(int y, int x){
        return 0 <= y && y< N && 0 <= x && x < N;
    }

    static void dfs(int y, int x){
        map[y][x] = cnt;
        for (int i=0; i<4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(inRange(ny,nx)){
                if(map[ny][nx]==1){
                    dfs(ny,nx);
                }else if (map[ny][nx]==0 && visit[ny][nx]==0){
                    visit[ny][nx]=1;
                    q.offer(new int[]{ny,nx});
                }
            }
        }
    }

    static void bfs(){
        while(!q.isEmpty()){
            int[] tmp = q.poll();
            int y = tmp[0];
            int x = tmp[1];
            for(int i=0; i<4; i++){
                int ny = y + dy[i];
                int nx = x + dx[i];
                if(inRange(ny,nx)){
                    if(map[ny][nx]==0){
                        if(visit[ny][nx]==0 && visit[y][x]<min){
                            visit[ny][nx] = visit[y][x]+1;
                            q.offer(new int[]{ny, nx});
                        }
                    } else if (map[ny][nx]!=cnt){
                        if(min>visit[y][x]){
                            min = visit[y][x];
                            return;
                        }
                    }
                }
            }
        }
    }
}