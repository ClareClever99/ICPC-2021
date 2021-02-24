package Practice_Problems.R2.Java;

import java.util.Scanner;

public class R2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            int r1 = sc.nextInt();
            int s = sc.nextInt();
            System.out.println((2 * s) - r1);
        }
        sc.close();
    }

}