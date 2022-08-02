package Baekjoon;
// 거스름돈
import java.util.Scanner;

public class B_5585 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int m = 1000 - n;
        int[] list = {500, 100, 50, 10, 5, 1};
        int cnt = 0;

        for (int i:list) {
            cnt += m/i;
            m = m%i;
        }

        System.out.println(cnt);
    }
}