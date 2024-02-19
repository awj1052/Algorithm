// BOJ 1071
// A[i] + 1 != A[i+1] 을 만족하지 않도록만 집중해서 사전순을 간과함
// 예제 입력에 중요한 정보가 없어서 더욱 그러한 듯
// 1 2 3 3 4 4 5 일 때 1 3 3 2 5 4 4 로 출력함. 답은 1 3 2 4 3 5 4
// 질문 검색에 테케 올려주신 것을 참고함
// A[i] > 0 이고 A[i+1] > 0 일 때 
// A[i+2]가 있다면 (A[i] 전부) + (A[i+2] 하나) + (A[i+1] 전부)
// A[i+2]가 없다면 (A[i+1] 전부) + (A[i] 전부) 

import java.util.Scanner;

public class BOJ {
    static int[] num;
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        num = new int[1001];
        int[] next = new int[1001];
        for(int i=0; i<N; i++){
            num[sc.nextInt()]+=1;
        }
        int last = 0;
        for(int i=1000; i>=0; i--){
            if (num[i] == 0) continue;
            next[i]=last; last=i;
        }
        for(int i=0; i<1001; i++) {
            if (num[i] == 0) continue;
            if (i!=1000 && num[i+1]>0){
                if(next[i+1]!=0){
                    print(i); System.out.print(next[i+1] + " "); num[next[i+1]]-=1;
                }else{
                    print(i+1); print(i); return;
                }
            } else {
                print(i);
            }
        }
    }

    public static void print(int n){
        for(int i=0; i<num[n]; i++){
            System.out.print(n + " ");
        }
    }
}
