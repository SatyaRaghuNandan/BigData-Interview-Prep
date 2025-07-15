```java

class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products);
        List<List<String>> res = new ArrayList();
        int[] searchSpace = new int[2];
        searchSpace[0] = 0;
        searchSpace[1] = products.length - 1;
        for(int i = 0; i<searchWord.length(); i++) {
            char c = searchWord.charAt(i);
            res.add(findWords(searchSpace, products, c,i));
        }
        return res;
    }     

    private List<String> findWords(int[] searchSpace, String[] products, char charAtindex, int charIndex) {
        int left = searchSpace[0], right = searchSpace[1];
        while(left<=right) {
            int mid = left + (right-left)/2;
            if(products[mid].length() <= charIndex || products[mid].charAt(charIndex) < charAtindex) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        searchSpace[0] = left;
        right = searchSpace[1];
        while(left<=right) {
            int mid = left+(right-left)/2;
            if(products[mid].length() <= charIndex || products[mid].charAt(charIndex) > charAtindex) {
                right = mid - 1;
            } else {
                left = mid+1;
            }
        }
        searchSpace[1] = right;
        List<String> ans = new ArrayList<>();

        for(int i =searchSpace[0]; i<searchSpace[0]+3 && i<=searchSpace[1]; i++ ) {
            ans.add(products[i]);
        }
        return ans;

    }
}


```
