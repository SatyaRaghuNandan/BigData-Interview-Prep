Question Asked in META.

Given a set of words, find the minimal subset that satisfies the following requirement: for every word X in the input, there exists a word Y in the output where Y is a prefix of X. Example input: ["the", "their", "there", "dog", "cat"]. The corresponding minimal subset satisfying the requirement is ["the", "dog", "cat"]. => (I suggested using Trie and the interviewer accepted: save all words as Trie data structure and then DFS traversing the tree.)
the -> the
their -> the
there -> the
dog -> dog
cat -> cat


Great observation! This problem is about **finding the minimal set of prefix roots** that **cover all words in the original list**. Your Trie + DFS approach is ideal and elegant for this.

---

## ✅ Problem Restated:

Given a list of words, return the **smallest subset** of these words such that **each input word has a prefix present in this subset**.

---

## ✅ Key Insight:

We want to keep only the **shortest prefix word** in the output if **longer words share the same prefix**.

---

## ✅ Approach: **Trie + DFS**

1. **Insert all words into a Trie**.
2. During insertion, mark end-of-word.
3. Then do a **DFS traversal**:

   * If a word ends at a node, **add it to the result** and **don’t traverse its children**.
   * This ensures we **don’t include longer words** if a shorter prefix already covers them.

---

## ✅ Java Code with Telugu Comments (Transliterated)

```java
import java.util.*;

class PrefixCover {
    // Trie Node class
    static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        boolean isEndOfWord = false;
        String word = null; // Ee node daggara word complete ayindi ante store cheyyadam kosam
    }

    // Root node of Trie
    TrieNode root = new TrieNode();

    // Step 1: Insert all words into Trie
    public void insert(String word) {
        TrieNode curr = root;
        for (char ch : word.toCharArray()) {
            curr = curr.children.computeIfAbsent(ch, c -> new TrieNode());
        }
        curr.isEndOfWord = true;
        curr.word = word;
    }

    // Step 2: DFS Traversal
    public void dfs(TrieNode node, List<String> result) {
        if (node.isEndOfWord) {
            result.add(node.word); // Prefix word ki saripothundi, inka children chudalsina avasaram ledu
            return;
        }
        for (TrieNode child : node.children.values()) {
            dfs(child, result);
        }
    }

    // Main function
    public List<String> minimalPrefixCover(String[] words) {
        for (String word : words) {
            insert(word);
        }

        List<String> result = new ArrayList<>();
        dfs(root, result);
        return result;
    }

    public static void main(String[] args) {
        PrefixCover pc = new PrefixCover();
        String[] input = {"the", "their", "there", "dog", "cat"};
        List<String> output = pc.minimalPrefixCover(input);
        System.out.println(output); // Output: [the, dog, cat]
    }
}
```

---

## ✅ Time and Space Complexity:

* **Insertion (Trie Build)**: O(N \* L), where N = number of words, L = average length
* **DFS Traversal**: O(T), where T = total number of Trie nodes (depends on character uniqueness)
* **Space**: O(T), where T = total Trie size

---

## ✅ Edge Cases:

* Empty input → return empty list
* All unique, non-overlapping words → return all
* All words are prefixes of each other → return shortest one only

---

Let me know if you want a Python version or dry run example on your input.
