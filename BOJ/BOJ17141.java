package lab09;

// BOJ 17141

import java.io.*;
import java.util.*;

public class BOJ {

    static int[] dy = {1,-1,0,0};
    static int[] dx = {0,0,1,-1};
    static int[][] map, spread;
    static ArrayList<int[]> virus;
    static int N,M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = br.readLine().split(" ");
        N = Integer.parseInt(tmp[0]); M = Integer.parseInt(tmp[1]);
        map = new int[N][N]; virus = new ArrayList<>(); spread = new int[N][N];;
        for(int i=0; i<N; i++){
            tmp = br.readLine().split(" ");
            for(int j=0; j<N; j++){
                map[i][j] = Integer.parseInt(tmp[j]);
                // 2가 입력되면 map은 0이라 해놓고 virus에 2의 위치를 기억해둠
                if(map[i][j] == 2){
                    virus.add(new int[]{i, j});
                    map[i][j]=0;
                }
            }
        }
        int ans = Integer.MAX_VALUE;
        // 비트마스크 virus.size()개의 원소중 M개의 원소 중복없이 추출
        for(int i=0; i<(1<<virus.size()); i++){
            if(Integer.bitCount(i)==M){

                for(int j=0; j<N; j++) {
                    System.arraycopy(map[j], 0, spread[j], 0, N);
                }
                Queue<int[]> q = new LinkedList<>();
                for(int j=0; j < virus.size(); j++){
                    if(((1<<j) & i) > 0){
                        q.offer(virus.get(j));
                        spread[virus.get(j)[0]][virus.get(j)[1]]=2;
                    }
                }
                ans = Math.min(ans, dfs(q));
            }
        }
        System.out.print((ans == Integer.MAX_VALUE) ? -1 : ans);
    }

    static int dfs(Queue<int[]> q){
        // 벽이 1이고 2 이상의 수가 바이러스가 퍼진 시간-2 임
        int time = 2;
        // dfs
        while(!q.isEmpty()){
            int[] tmp = q.poll();
            int y = tmp[0]; int x = tmp[1];
            for(int i=0; i<4; i++){
                int ny = y + dy[i]; int nx = x + dx[i];
                if(Range(ny, nx) && spread[ny][nx]==0){
                    spread[ny][nx] = spread[y][x]+1;
                    q.offer(new int[]{ny, nx});
                    if(spread[ny][nx] > time) time=spread[ny][nx];
                }
            }
        }
        // 0 이 있는지 확인
        for(int n=0; n<N; n++){
            for(int m=0; m<N; m++){
                if(spread[n][m]==0){
                    // -1 을 출력하고 exit 했으나 예외가 있어 방식을 변경함
                    return Integer.MAX_VALUE;
                }
            }
        }
        return time-2;
    }

    static boolean Range(int y, int x){
        return 0 <= y && y < N && 0<= x && x < N;
    }
}