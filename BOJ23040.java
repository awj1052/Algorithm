package lab09;

// BOJ 23040

import java.io.*;
import java.util.*;

public class BOJ {

    static ArrayList<ArrayList<Integer>> line;
    static int N;
    static char[] color;
    static long[] nutella;
    static int[] visit;
    static Stack<Integer> stack;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        line = new ArrayList<>(); stack = new Stack<>();
        N = Integer.parseInt(br.readLine());
        // visit을 boolean으로 했다가 예외가 있음을 알고 int로 변경
        nutella = new long[N]; visit = new int[N];
        for(int i=0; i<N; i++){
            line.add(new ArrayList<>());
        }
        for(int i=1; i<N; i++){
            String[] tmp = br.readLine().split(" ");
            int a = Integer.parseInt(tmp[0])-1; int b = Integer.parseInt(tmp[1])-1;
            line.get(a).add(b); line.get(b).add(a);
        }
        color = br.readLine().toCharArray();
        br.close();
        // 습관적으로 int형으로 선언했다가 낭패 봤다..
        long ans = 0L;
        for(int i=0; i<N; i++){
            if(color[i]=='B'){
                ans += nutella(i, i);
            }
        }
        System.out.println(ans);
    }

    static long nutella(int to, int from){
        if(nutella[to]>0L) return nutella[to];
        if(color[to]!='B') stack.add(to); // return 될 수 있으므로 add 호출을 적절한 위치에 둬야함
        long res = 0L;
        for(int m : line.get(to)) {
            // visit[m] == from 으로 했다가 기본값인 0과 from=0 과 겹쳐서 +1해줌
            if (color[m] == 'B' || visit[m] == from+1) continue;
            visit[m] = from+1;
            long cnt = nutella(m, from);
            res+=cnt+1L;
            if (color[to] == 'B') {
                while (!stack.isEmpty()) {
                    nutella[stack.pop()] = cnt;
                }
            }
        }
        return res;
    }
}