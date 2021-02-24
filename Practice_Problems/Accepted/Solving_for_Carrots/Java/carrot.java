package Practice_Problems.Passed.Solving_for_Carrots.Java;

import java.util.Scanner;

public class carrot {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            long contestants = sc.nextLong();
            long problemsSolved = sc.nextLong();
            for (int i = 0; i <= contestants; i++) {
                sc.nextLine();
            }
            System.out.println(problemsSolved);
        }
        sc.close();
    }

}