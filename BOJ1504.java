import java.util.*;
import java.io.*;

class Pair implements Comparable<Pair>{
    int x,y;
    Pair(int x, int y){ this.x=x; this.y=y; }
    @Override
    public int compareTo(Pair o) {
        return y-o.y;
    }
}

public class BOJ {
    static final int INF = 3*800*1000 + 1;
    static ArrayList<Pair>[] line;
    static int V;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = br.readLine().split(" ");
        V = Integer.parseInt(tmp[0]); int E = Integer.parseInt(tmp[1]);
        line = new ArrayList[V+1];
        for(int i=1; i<=V; i++) line[i] = new ArrayList<>();
        for(int i=0; i<E; i++) {
            tmp = br.readLine().split(" ");
            line[Integer.parseInt(tmp[0])].add(new Pair(Integer.parseInt(tmp[1]), Integer.parseInt(tmp[2])));
            line[Integer.parseInt(tmp[1])].add(new Pair(Integer.parseInt(tmp[0]), Integer.parseInt(tmp[2])));
        }
        tmp = br.readLine().split(" ");
        int v = Integer.parseInt(tmp[0]); int w = Integer.parseInt(tmp[1]);
        int[] d = dijkstra(1);
        int[] dv = dijkstra(v);
        int[] dw = dijkstra(w);

        // 1 -> v -> w -> N
        // d[v] + dv[w] + dw[V]
        // 1 -> w -> v -> N
        // d[w] + dw[v] + dv[N]
        int ans = Math.min(d[v] + dv[w] + dw[V], d[w] + dw[v] + dv[V]);
        if (ans>=INF || ans<0){
            System.out.println(-1);
        }else{
            System.out.println(ans);
        }

    }
    static int[] dijkstra(int start){
        int[] d = new int[V+1];
        for(int i=1; i<=V; i++){
            d[i]=INF;
        }
        d[start]=0;
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        pq.add(new Pair(start, 0));
        while(!pq.isEmpty()){
            Pair P = pq.poll();
            if(d[P.x] < P.y) continue;
            for(Pair p : line[P.x]){
                if(d[P.x] + p.y >= d[p.x]) continue;
                d[p.x] = d[P.x] + p.y;
                pq.add(new Pair(p.x, d[p.x]));
            }
        }
        return d;
    }
}
