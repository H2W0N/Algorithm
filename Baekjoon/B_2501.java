package Baekjoon;

// 약수 구하기
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class B_2501 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int k = s.nextInt();

        List<Integer> list = new ArrayList<>();

        for (int i=1; i<=n; i++) {
            if (n%i == 0) {
                list.add(i);
            }
        }

        if (list.size()>=k) {
            System.out.println(list.get(k-1));
        }
        else {
            System.out.println(0);
        }
        
    }
}