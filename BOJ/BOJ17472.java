import java.io.*;
import java.util.*;

class Point {
	int y;
	int x;
	public Point(int y, int x) {
		this.y = y;
		this.x = x;
	}
}

class Pair implements Comparable<Pair>{
	int dest;
	int cost;
	public Pair(int dest, int cost) {
		this.dest = dest;
		this.cost = cost;
	}
	public int compareTo(Pair o) {
		return cost - o.cost;
	}	
}

public class Main {
	
	private static final int INIT_LANDMARK = 2;
	private static final int[] dx = {0,0,1,-1};
	private static final int[] dy = {1,-1,0,0};
	private static int[][] graph;
	private static ArrayList<Pair>[] line;
	private static int N;
	private static int M;

	public static void main(String[] args) throws IOException {
		Main main = new Main();
		BufferedReader br = main.getReader();
		int[] temp = main.getInt(br);
		N = temp[0];
		M = temp[1];
		graph = new int[N][M];
		for (int i=0; i<N; i++) {
			temp = main.getInt(br);
			for(int j=0; j<M; j++) {
				graph[i][j] = temp[j];
			}
		}
		System.out.println(main.solve());
	}
	
	private int solve() {
		int landMark = INIT_LANDMARK;
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if (graph[i][j] != 1) continue;
				findLand(i, j, landMark);
				landMark++;
			}
		}
		
		line = new ArrayList[landMark];
		for (int i=INIT_LANDMARK; i<landMark; i++) {
			line[i] = new ArrayList<Pair>();
		}
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(graph[i][j] == 0) continue;
				for(int dir=0; dir<4; dir++) {
					findBridge(i, j, dir, graph[i][j], 0);
				}
			}
		}
		
		PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
		HashSet<Integer> visit = new HashSet<Integer>();
		int cur = INIT_LANDMARK;
		int ans = 0;
		for (int i=INIT_LANDMARK; i<landMark; i++) {
			visit.add(cur);
			line[cur].forEach(pq::add);
			while (!pq.isEmpty()) {
				Pair poll = pq.poll();
				if (!visit.contains(poll.dest)) {
					cur = poll.dest;
					ans = ans + poll.cost;
					break;
				}
			}
		}
		return visit.size() == landMark - INIT_LANDMARK ? ans : -1;
	}
	
	private void findLand(int initY, int initX, int landMark) {
		Queue<Point> queue = new LinkedList<Point>();
		queue.add(new Point(initY, initX));
		graph[initY][initX] = landMark;
		while (!queue.isEmpty()) {
			Point poll = queue.poll();
			for (int dir=0; dir<4; dir++) {
				int ny = dy[dir] + poll.y;
				int nx = dx[dir] + poll.x;
				if (isOutofRange(ny, nx)) continue;
				if (graph[ny][nx] != 1) continue;
				graph[ny][nx] = landMark;
				queue.add(new Point(ny, nx));
			}
		}
	}
	
	private void findBridge(int y, int x, int dir, int landMark, int distance) {
		int ny = dy[dir] + y;
		int nx = dx[dir] + x;
		if (isOutofRange(ny, nx)) return;
		int otherLandMark = graph[ny][nx];
		if (otherLandMark == landMark) return;
		if (otherLandMark == 0) {
			findBridge(ny, nx, dir, landMark, distance+1);
			return;
		}
		if (distance < 2) return;
		line[landMark].add(new Pair(otherLandMark, distance));
		line[otherLandMark].add(new Pair(landMark, distance));
	}
	
	private boolean isOutofRange(int y, int x) {
		return y >= N || y < 0 || x >= M || x < 0;
	}

	private BufferedReader getReader() {
		return new BufferedReader(new InputStreamReader(System.in));
	}
	
	private int[] getInt(BufferedReader br) throws IOException {
		return Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
	}
}
