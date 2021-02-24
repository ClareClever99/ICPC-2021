package Practice_Problems.Accepted.Stuck_In_A_Time_Loop.Java;

import java.util.Scanner;

public class time {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLong()) {
            long input = sc.nextLong();
            for (int i = 0; i < input; i++) {
                System.out.println((i + 1) + " Abracadabra");
            }
        }
        sc.close();
    }

}