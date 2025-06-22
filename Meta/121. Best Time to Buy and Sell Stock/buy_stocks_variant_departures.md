import java.util.*;

public class TicketFinder {

    public static int findCheapestTickets(int[] departures, int[] returns) {
        int minDepartureCost = departures[0];
        int minCost = Integer.MAX_VALUE;

        // Start from index 1 since we're comparing with minDepartureCost
        for (int i = 1; i < departures.length; i++) {
            // Check current min departure + current return cost
            minCost = Math.min(minCost, minDepartureCost + returns[i]);

            // Update the minimum departure cost seen so far
            if (departures[i] < minDepartureCost) {
                minDepartureCost = departures[i];
            }
        }

        return minCost;
    }

    public static void main(String[] args) {
        assert findCheapestTickets(new int[]{8, 3, 6, 10}, new int[]{10, 9, 5, 8}) == 8;
        assert findCheapestTickets(new int[]{10, 3, 10, 9, 3}, new int[]{4, 20, 6, 7, 10}) == 9;
        assert findCheapestTickets(new int[]{1, 3, 10, 9, 3}, new int[]{1, 20, 6, 7, 10}) == 7;
        assert findCheapestTickets(new int[]{1, 3, 10, 9, 3}, new int[]{1, 1, 6, 7, 10}) == 2;
        assert findCheapestTickets(new int[]{1, 3, 10, 9, 3}, new int[]{10, 9, 8, 7, 6}) == 7;
        assert findCheapestTickets(new int[]{12, 33, 44, 9, 23}, new int[]{100, 90, 80, 70, 15}) == 24;
        assert findCheapestTickets(new int[]{4, 3, 5, 11, 2}, new int[]{1, 6, 10, 2, 9}) == 5;

        System.out.println("All test cases passed!");
    }
}
