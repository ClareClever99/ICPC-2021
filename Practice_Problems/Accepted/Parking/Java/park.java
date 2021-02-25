package Practice_Problems.Accepted.Parking.Java;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class park {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> listOfStores = new ArrayList<Integer>();
        long numTests = sc.nextLong();
        int totalDistance = 0;
        while (sc.hasNextLong()) {
            for (int i = 0; i < numTests; i++) {
                // Reset values
                listOfStores.clear();
                totalDistance = 0;

                long numStores = sc.nextLong();

                for (int j = 0; j < numStores; j++) {
                    listOfStores.add(sc.nextInt());
                }

                // Sort the list
                Collections.sort(listOfStores);

                for (int index = 0; index < listOfStores.size() - 1; index++) {
                    totalDistance += listOfStores.get(index + 1) - listOfStores.get(index);
                }
                System.out.println(totalDistance * 2);
            }
        }
        sc.close();
    }
}
