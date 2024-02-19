import java.io.*;
import java.util.*;

public class BOJ {

    static char[] l, letter;
    static int L,C;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = br.readLine().split(" ");
        L = Integer.parseInt(tmp[0]); C = Integer.parseInt(tmp[1]);
        letter = new char[C]; l = new char[L];
        tmp = br.readLine().split(" ");
        for(int i=0; i<C; i++){
            letter[i] = tmp[i].charAt(0);
        }
        Arrays.sort(letter);
        f(0, 0);

    }

    public static void f(int n, int m){
        if(n==L){
            if(!b()) return;
            for(char c : l){
                System.out.print(c);
            }
            System.out.println();
            return;
        }

        for(int i=m; i<C; i++){
            l[n] = letter[i];
            f(n+1, i+1);
        }
    }

    // 자음 2개이상, 모음 1개이상
    public static boolean b(){
        int con = 0; int vow = 0;
        for(char c : l){
            if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'){
                vow+=1;
            }else{
                con+=1;
            }
        }
        return vow > 0 && con > 1;
    }
}
