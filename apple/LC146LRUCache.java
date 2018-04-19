class Node {
    int key;
    int value;
    Node prev;
    Node next;
    public Node(int key, int value) {
        this.key = key;
        this.value = value;
    }
}

public class LRUCache {
    HashMap<Integer, Node> hm;
    int capacity;
    int count;
    Node head;
    Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        hm = new HashMap<>();
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
        head.prev = null;
        tail.next = null;
        count = 0;
    }

    public int get(int key) {
        if (!hm.containsKey(key)) return -1;
        else {
            Node node = hm.get(key);
            int value = node.value;
            deleteNode(node);
            addNode(node);
            return value;
        }
    }

    public void addNode(Node node) {
        Node temp = tail.prev;
        temp.next = node;
        node.next = tail;
        tail.prev = node;
        node.prev = temp;
    }

    public void deleteNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public void put(int key, int value) {
        if (!hm.containsKey(key)) {
            Node node = new Node(key, value);
            hm.put(key, node);
            if (count < capacity) {
                count++;
                addNode(node);
            } else {
                hm.remove(head.next.key);
                deleteNode(head.next);
                addNode(node);
            }
        } else {
            Node node = hm.get(key);
            node.value = value;
            deleteNode(node);
            addNode(node);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
