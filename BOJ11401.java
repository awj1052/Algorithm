package lab09;

// BOJ 11401

// 95%에서 실패했는데 확인해보니 0! 을 0으로 리턴하게 해버린 것.
// mod p를 위한 펙토리얼 및 제곱 연산을 재정의
// 페르마의 소정리 -> a는 정수, p는 소수이며 a를 p로 나눌 수 없을 때
// a^p == a (mod p) -> a^(p-1) == 1 (mod p) -> a * a^(p-2) == 1 (mod p)
// mod p 연산에 대해 a의 역원은 a^(p-2)
// (n/m)%p <=> (n*m^(-1))%p (단, n,m은 서로소, m^(-1) 은 mod p 연산에 대한 m의 역원)

import java.util.Scanner;

public class BOJ {

    static final long MOD = 1_000_000_007L;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextInt();
        long K = sc.nextInt();
        sc.close();
        // 페르마의 소정리
        System.out.println(factorial(N) * pow(factorial(N-K) * factorial(K)%MOD,MOD-2) % MOD);
    }

    static long factorial(long n){
        if(n==0){
            return 1;
        }
        long res = n;
        while(n-->2){
            res = res*n%MOD; // res *= n%MOD 와 다름
        }
        return res;
    }

    static long pow(long n, long k){
        if(k==1){
            return n%MOD;
        }
        long res = pow(n, k / 2);
        if((k & 1) == 1){
            return (res*res%MOD)*n%MOD;
        }
        return res*res%MOD;

    }
}