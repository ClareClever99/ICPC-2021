package Practice_Problems.Passed.Coldputer_Science.Java;

import java.util.ArrayList;
import java.util.Scanner;

public class cold {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLong()) {
            ArrayList<Integer> list = new ArrayList<Integer>();
            long num = sc.nextLong();
            int temps = 0;
            for (int i = 0; i < num; i++) {
                list.add(sc.nextInt());
            }

            for (Integer integer : list) {
                if (integer < 0) {
                    temps++;
                }
            }
            System.out.println(temps);
        }
        sc.close();
    }
}
