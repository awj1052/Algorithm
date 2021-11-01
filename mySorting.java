package lab07;

import java.lang.reflect.Field;
import java.util.*;

class myNum{
    int a, b;

    myNum(int a, int b){
        this.a=a;
        this.b=b;
    }
    public String toString(){
        return this.a + " " + this.b;
    }
    @Override
    public boolean equals(Object other){
        if (!(other instanceof myNum)) return false;
        myNum o = (myNum) other;
        if(this.a==o.a && this.b==o.b){
            return true;
        }
        return false;
    }
}

class myComp implements Comp<myNum>{

    @Override
    public int compareTo(myNum a, myNum b) {
        if (a.a != b.a) return a.a - b.a;
        return a.b-b.b;
    }
}

public class mySorting {

    public static void main(String[] args){
        ArrayList<myNum> n = new ArrayList<>();
        ArrayList<myNum> nn = new ArrayList<>();
        for(int i=0; i<60000; i++){
            int a = (int) (Math.random()*100000)-50000;
            int b = (int) (Math.random()*100000)-50000;
            n.add(new myNum(a,b));
            nn.add(new myNum(a,b));
        }
        long start = System.currentTimeMillis();
        mySort.sort(n, new myComp());
        System.out.println("-----mySort-----");
        System.out.println("걸린 시간 : " + (System.currentTimeMillis()-start) + "ms");
        start = System.currentTimeMillis();
        Collections.sort(nn, (i,j) -> { if(i.a!=j.a) { return i.a-j.a; } else { return i.b-j.b; }});
        System.out.println("-----Collection-----");
        System.out.println("걸린 시간 : " + (System.currentTimeMillis()-start) + "ms");
        for (int i=0; i<n.size(); i++){
            if(!n.get(i).equals(nn.get(i))){
                System.out.println("다름");
                System.exit(0);
            }
        }
        System.out.println("같음");

        // 평균 각각 70ms씩 나옴
        // 정렬 결과는 같음
        // 대체로 Collections.sort가 더 좋은 성능을 보임.
        // 경우에 따라선 mySort(Quick Sort)도 좋은 성능을 보임.
        // 극단적으로 mySort 78ms, Collections.sort 47ms 와 같이 차이남
        // 둘다 100ms 넘을 때도 있고.
    }
}

interface Comp<T>{
    public int compareTo(T a, T b);
}

class mySort{

    static Comp cc = null;

    public static <T> void sort(List<T> data, Comp<? super T> c){
        cc = c;
        quick(data, 0, data.size()-1);

    }

    public static <T> void quick(List<T> data, int start, int end){
        if (start >= end) return;
        int pv = pivot(data, start, end);
        quick(data, start, pv-1);
        quick(data, pv+1, end);
    }

    public static <T> int pivot(List<T> data, int start, int end){
        T pv = data.get(start);
        int low = start + 1;
        int high = end;
        while(true){
            while(low<=high && cc.compareTo(data.get(low), pv) <= 0){ // data.get(low) <= pv
                low++;
            }
            while(low<=high && cc.compareTo(pv, data.get(high)) <= 0){ // pv <= data.get(high)
                high--;
            }
            if(high<low){
                break;
            }else{
                T tmp = data.get(low);
                data.set(low, data.get(high));
                data.set(high, tmp);
            }
        }
        T tmp = data.get(start);
        data.set(start, data.get(high));
        data.set(high, tmp);
        return high;
    }
}
