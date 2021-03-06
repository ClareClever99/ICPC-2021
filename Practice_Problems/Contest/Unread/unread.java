package Practice_Problems.Contest.Unread;

import java.util.Scanner;

public class unread {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String firstLine = sc.nextLine();

        String[] arrOfStr = firstLine.split(" ");

        int n = Integer.parseInt(arrOfStr[0]);
        int m = Integer.parseInt(arrOfStr[1]);
        int[] lastIndex = new int[n];

        for (int i = 0; i < lastIndex.length; i++) {
            lastIndex[i] = 0;
        }

        int unread = 0;

        for (int i = 0; i < m; i++) {
            int num = sc.nextInt();
            unread += (n - 1) - (i - lastIndex[num - 1]);
            lastIndex[num - 1] = i + 1;
            System.out.println(unread);
        }

        sc.close();
    }

}