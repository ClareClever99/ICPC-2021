package Practice_Problems.R2.Java;

import java.util.Scanner;

public class R2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        while (!(line.isEmpty())) {
            String[] list = line.split(" ");
            int r1 = Integer.parseInt(list[0]);
            int s = Integer.parseInt(list[1]);
            System.out.println((2 * s) - r1);
            line = sc.nextLine();
        }
        sc.close();
    }

}