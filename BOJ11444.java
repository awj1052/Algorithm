import java.util.*;

public class BOJ {
    static int MOD = 1000000007;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long[][] A = new long[][]{{0,1},{1,1}};
        long N = sc.nextLong();
        System.out.println(pow(A,N));
    }
    static long pow(long[][] A, long b){
        long[][] res = new long[][]{{1,0},{0,1}};
        while (b>0){
            if(b%2==1){
                res = mul(res, A);
                b-=1;
            }
            A = mul(A, A);
            b/=2;
        }
        return res[0][1];
    }
    static long[][] mul(long[][] A, long[][] B){
        long[][] C = new long[2][2];
        C[0][0] = (A[0][0]*B[0][0]%MOD + A[0][1]*B[1][0]%MOD)%MOD;
        C[0][1] = (A[0][0]*B[0][1]%MOD + A[0][1]*B[1][1]%MOD)%MOD;
        C[1][0] = (A[1][0]*B[0][0]%MOD + A[1][1]*B[1][0]%MOD)%MOD;
        C[1][1] = (A[1][0]*B[0][1]%MOD + A[1][1]*B[1][1]%MOD)%MOD;
        return C;
    }
}
