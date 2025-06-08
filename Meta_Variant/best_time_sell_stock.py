Given two arrays representing bus ticket prices for departures and returns, respectively, where the index corresponds to the timestamp (in days) and the value represents the price, the task is to find the minimum cost of purchasing a valid pair of tickets. The return ticket must be for a date on or after the corresponding departure's day.
For instance, consider the arrays departure = [10, 3, 10, 9, 3] and return = [4, 20, 6, 7, 10]. The minimum cost for a valid pair is 3 + 6 = 9.



  public static int findMinCost(int[] departurePrices, int[] returnPrices) {
        int minCost = Integer.MAX_VALUE;
        int[] minReturnFromDay = new int[returnPrices.length];

        // Initialize the last day with its own return price
        minReturnFromDay[minReturnFromDay.length - 1] = returnPrices[returnPrices.length - 1];

        // Calculate cheapest valid return from each day (working backwards)
        for (int i = returnPrices.length - 2; i >= 0; i--) {
            minReturnFromDay[i] = Math.min(returnPrices[i], minReturnFromDay[i + 1]);
        }

        // Find minimum cost considering valid returns
        for (int i = 0; i < departurePrices.length; i++) {
            minCost = Math.min(minCost, departurePrices[i] + minReturnFromDay[i]);
        }

        return minCost;
    }
	
	
Is just a variant of Buying and Selling Stocks I.
def find_cheapest(departure, ret):
    min_return_price_idx = len(ret) - 1
    min_cost = float("inf")
    for i in range(len(ret) - 1, -1, -1):
        if ret[i] < ret[min_return_price_idx]:
            min_return_price_idx = i

        min_cost = min(min_cost, departure[i] + ret[min_return_price_idx])

    return min_cost if min_cost != float("inf") else -1





def find_cheapest_tickets(departures, returns):
    min_departure_cost = departures[0]
    min_cost = float('inf')
    
    for i in range(1, len(departures)):
        min_cost = min(min_cost, min_departure_cost + returns[i])

        if departures[i] < min_departure_cost:
            min_departure_cost = departures[i]
    
    return min_cost

if __name__ == "__main__":
    departures = [8, 3, 6, 10]
    returns = [10, 9, 5, 8]
    assert find_cheapest_tickets(departures, returns) == 8

    departures = [10, 3, 10, 9, 3]
    returns = [4, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 9

    departures = [1, 3, 10, 9, 3]
    returns = [1, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [1, 3, 10, 9, 3]
    returns = [1, 1, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 2

    departures = [1, 3, 10, 9, 3]
    returns = [10, 9, 8, 7, 6]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [12, 33, 44, 9, 23]
    returns = [100, 90, 80, 70, 15]
    assert find_cheapest_tickets(departures, returns) == 24

    departures = [4, 3, 5, 11, 2]
    returns = [1, 6, 10, 2, 9]
    assert find_cheapest_tickets(departures, returns) == 5


