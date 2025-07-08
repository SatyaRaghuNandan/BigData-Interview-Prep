Screening:

Q1: 680. Valid Palindrome II => follow-up: 12116: Valid Palindrome III (just asked for the signature of recursive call)

On-site:
ML system design: Design an add prediction for facebook Reels.

Coding:

Merge Two Sorted Interval Arrays: Given two sorted, non-overlapping interval lists, return a 3rd interval list that is the union of the input interval lists. (variation of 986. Interval List Intersections)

City Generator
Given a list of city names and their corresponding populations, write a program to output a city name subject to the following constraint: the probability of the program to output a city's name is based on its population divided by the sum of all cities' population. Assume the program will be repeatedly called many times. [1,2,3,4]

Write a function that, given a binary tree of integers, returns the sums of all the root-to-leaf paths. (variation 129. Sum Root to Leaf Numbers)

Given a set of words, find the minimal subset that satisfies the following requirement: for every word X in the input, there exists a word Y in the output where Y is a prefix of X. Example input: ["the", "their", "there", "dog", "cat"]. The corresponding minimal subset satisfying the requirement is ["the", "dog", "cat"]. => (I suggested using Trie and the interviewer accepted: save all words as Trie data structure and then DFS traversing the tree.)
the -> the
their -> the
there -> the
dog -> dog
cat -> cat
---------------




private int binarySearch(int target, List<int[]> list) {
        int l = 0, r = list.size() - 1;
        while (l <= r) { // Left <= right anukunnamu. 
            int mid = l + (r - l) / 2;
            int midIndex = list.get(mid)[0];
            if (midIndex == target) {
                return list.get(mid)[1];
            } else if (midIndex < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return 0;
    }
	



// Time: O(n)
// Space: O(1) (since digits max = 10)

class Solution {

    public int maximumSwap(int num) {
        // First Integer ni String lo Convert chesi and Char Array loki convert chesaru. 
        char[] digits = Integer.toString(num).toCharArray();
        int[] rightMostIndex = new int[10]; // SImilar to a - z  26 length Laga. we have 10.
        for (int i = 0; i< digits.length;i++) {
            rightMostIndex[digits[i] - '0'] = i; // You are not incrementing but, 
        }

        for (int i = 0; i < digits.length; i++) {
            for (int d = 9; d > digits[i] - '0'; d--) {
                if (rightMostIndex[d] > i) {
                    char temp = digits[i];
                    digits[i] = digits[rightMostIndex[d]];
                    digits[rightMostIndex[d]] = temp;

                    return Integer.parseInt(new String(digits));
                }
            }
        }
        return num;
    }
}
