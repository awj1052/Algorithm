package lab09;

// BOJ 1707

// 간선 정보를 boolean[][] 으로 하니 메모리 초과가 나서 ArrayList로 변경
// 이분 그래프 -> 모든 정점을 A집합과 B집합, 2가지로 나눈다고 할 떼
// 자신의 인접한 노드를 자신과 다른 집합에 속하도록 한다.
// 인접한 노드가 이미 잡합에 속해있는데 자신과 같은 집합이면 그것은 이분 그래프가 아니다.

import java.io.*;
import java.util.*;

public class BOJ {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        loop: while(tc-->0) {
            String[] tmp = br.readLine().split(" ");
            int v = Integer.parseInt(tmp[0]);
            ArrayList<ArrayList<Integer>> l = new ArrayList<>();
            int[] visit = new int[v+1];
            int e = Integer.parseInt(tmp[1]);

            for(int i=0; i<v+1; i++){
                l.add(new ArrayList<>());
            }

            while (e-- > 0) {
                tmp = br.readLine().split(" ");
                int a = Integer.parseInt(tmp[0]);
                int b = Integer.parseInt(tmp[1]);
                l.get(a).add(b);
                l.get(b).add(a);
            }
            for(int k=1; k<=v; k++) {
                if(visit[k]!=0) continue;
                Queue<Integer> q = new LinkedList<>();
                visit[k] = 1;
                q.offer(k);
                while (!q.isEmpty()) {
                    int i = q.poll();
                    for (int j : l.get(i)) {
                        if (visit[j] == 0) {
                            visit[j] = -1 * visit[i];
                            q.offer(j);
                        } else if (visit[j] == visit[i]) {
                            System.out.println("NO");
                            continue loop;
                        }
                    }
                }
            }
            System.out.println("YES");
        }
    }
}