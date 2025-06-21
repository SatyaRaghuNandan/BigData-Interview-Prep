MovingAverage




  [Java] Sliding Window based approach

Code
class MovingAverage {

    Queue<Integer> queue;
    int windowSum;
    int size;

    public MovingAverage(int size) {
        this.size = size;
        this.windowSum = 0;
        this.queue = new LinkedList<>();
    }
    
    public double next(int val) {
        if(queue.size() < size) {
            //queue has capacity
            queue.add(val);
            windowSum += val;

            return (double) windowSum/queue.size();
        }

        //here means queue is full
        int removedValue = queue.remove();
        windowSum -= removedValue;

        queue.add(val);
        windowSum += val;

        return (double) windowSum/queue.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
A variant of this problem:
Incase the problem gives entire nums[] as input and asks to calculate movingAverageResult for each window of size k
That's a fixed size sliding window problem. Very simple.

//Instead of next() API, we get the full list as input
/*
    Given a list of integers 'nums' and an integer size, compute the average of elements
    in a sliding window of exactly size elements

    Return a list containing the result of these computations using Integer division
 */
public class MovingAverageFromDataStream {

    private int[] findMovingAverage(int[] nums, int k) {

        if(nums == null || nums.length == 0) {
            return new int[0];
        }

        int n = nums.length;
        int[] movingAverageResult = new int[n-k+1];
        int index = 0;

        int windowStart = 0, windowEnd = 0;

        int windowSum = 0;

        while(windowEnd < n) {
            windowSum += nums[windowEnd];

            //check if window has reached size of k
            if(windowEnd - windowStart + 1 == k) {
                movingAverageResult[index++] = windowSum/k;

                //shift the window
                windowSum -= nums[windowStart];
                windowStart++;
            }

            windowEnd++;
        }

        return movingAverageResult;
    }

    public static void main(String[] args) {
        MovingAverageFromDataStream obj = new MovingAverageFromDataStream();

        int[] nums = new int[] {5, 2, 8, 14, 3};
        int k = 3;
        int[] movingAverageResult = obj.findMovingAverage(nums, k);

        System.out.println("Moving average result: ");
        for(int value: movingAverageResult) {
            System.out.print(value + ", ");
        }
    }
}





