```java

class LRUCache {
    int capacity;
    Map<Integer, ListNode> dict; 
    ListNode head;
    ListNode tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        dict = new HashMap<>();
        head = new ListNode(-1, -1);
        tail = new ListNode(-1, -1);
        head.next = tail;
        tail.previous = head; 
    }

    public int get(int key) {
        if (!dict.containsKey(key)) {
            return -1;
        }
        ListNode node = dict.get(key);
        remove(node);
        addToHead(node);
        return node.value;
    }   

    public void put(int key, int value) {   
        if (dict.containsKey(key)) {
            ListNode oldNode = dict.get(key);
            remove(oldNode);
        }
        ListNode newNode = new ListNode(key, value);
        dict.put(key, newNode);
        addToHead(newNode);

        if (dict.size() > capacity) {
            ListNode nodeToDelete = head.next;
            remove(nodeToDelete);
            dict.remove(nodeToDelete.key);
        }
    }

    private void addToHead(ListNode node) {
        // Mundu Node 
        ListNode previousEnd = tail.previous; // get the Tail .next. 
        previousEnd.next = node; 
        // 
        node.previous = previousEnd;
        node.next = tail;
        tail.previous = node;
    }

    private void remove(ListNode node) {
        node.previous.next = node.next;
        node.next.previous = node.previous;
    }
}
```
