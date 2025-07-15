class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int ret = 0, power = 31;
        while (n != 0) {
            ret += (n & 1) << power;
            n = n >>> 1;
            power -= 1;
        }
        return ret;
    }
}
/**
O(1) TC 
O(1) SC
*/
