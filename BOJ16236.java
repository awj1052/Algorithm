package lab09;

// BOJ 16236

// 위, 왼쪽이 우선순위
// 같은 거리에 있고 먹을 수 있는 물고기들의 좌표를 ArrayList<int[]> fish 에 add하고
// fish를 순회하면서 (y,x) 를 우선순위에 맞게 해서 fish 중 하나의 원소만 선택
// BFS 순회 방식, 즉 dy, dx 배열을 적절히 바꾸면 될 줄 알았는데 아니였음. (TC 4)
// dy, dx의 순서는 상관 X

import java.io.*;
import java.util.*;

public class BOJ {

    static final int[] dy = {-1,0,1,0};
    static final int[] dx = {0,1,0,-1};

    static int[][] map;
    static int size, cnt, N, ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        size=2; cnt=0; ans=0;
        int y = 0, x = 0;
        for (int i = 0; i < N; i++) {
            String[] tmp = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(tmp[j]);
                if (map[i][j] == 9) {
                    y = i; x = j;
                    map[i][j]=0;
                }
            }
        }
        br.close();
        while(y != -1){
            int[] tmp = dfs(y,x);
            y=tmp[0];
            x=tmp[1];
        }
        System.out.println(ans);
    }

    static int[] dfs(int i, int j){
        int[][] visit = new int[N][N];
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{i,j});
        visit[i][j]=1;

        int distance = Integer.MAX_VALUE;
        ArrayList<int[]> fish = new ArrayList<>();

        while(!q.isEmpty()){
            int[] tmp = q.poll();
            int y = tmp[0];
            int x = tmp[1];
            for(int a=0; a<4; a++){
                int ny = y + dy[a];
                int nx = x + dx[a];
                if(inRange(ny,nx) && visit[ny][nx] == 0 && map[ny][nx] <= size){
                    if(map[ny][nx] > 0 && map[ny][nx] != size && visit[y][x] <= distance) {
                        distance = visit[y][x];
                        fish.add(new int[]{ny,nx});
                    }
                    visit[ny][nx]=visit[y][x]+1;
                    q.offer(new int[]{ny,nx});
                }
            }
        }
        if(!fish.isEmpty()){
            int min_y = Integer.MAX_VALUE, min_x = Integer.MAX_VALUE;
            for(int[] f : fish){
                if(f[0] < min_y){
                    min_y=f[0]; min_x=f[1];
                }else if(f[0] == min_y && f[1] < min_x){
                    min_x=f[1];
                }
            }
            cnt += 1;
            map[min_y][min_x] = 0;
            ans += visit[min_y][min_x]-1;
            if (cnt == size) {
                cnt = 0;
                size += 1;
            }
            return new int[]{min_y, min_x};
        }
        return new int[]{-1,-1};
    }

    static boolean inRange(int y, int x){
        return 0 <= y && y < N && 0 <= x && x < N;
    }
}