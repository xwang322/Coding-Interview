class MaxStack {
    class Node{
        int val;
        Node prev;
        Node next;
    }
    Node head = new Node();
    Node tail = new Node();
    TreeMap<Integer, List<Node>> map;

    public void addToTail(Node node) {
        Node temp = tail.prev;
        node.next = tail;
        tail.prev = node;
        node.prev = temp;
        temp.next = node;
    }

    public void removeFromList(Node node) {
        Node temp1 = node.prev;
        Node temp2 = node.next;
        temp1.next = temp2;
        temp2.prev = temp1;
    }

    /** initialize your data structure here. */
    public MaxStack() {
        head.next = tail;
        tail.prev = head;
        head.val = Integer.MIN_VALUE;
        tail.val = Integer.MIN_VALUE;
        map = new TreeMap<>();
    }

    public void push(int x) {
        List<Node> list = map.getOrDefault(x, new ArrayList<Node>());
        Node node = new Node();
        node.val = x;
        addToTail(node);
        list.add(node);
        map.put(x, list);
    }

    public int pop() {
        Node node = tail.prev;
        removeFromList(node);
        List<Node> list = map.get(node.val);
        list.remove(list.size()-1);
        if (list.size() == 0){
            map.remove(node.val);
        } else {
            map.put(node.val, list);
        }
        return node.val;
    }

    public int top() {
        return tail.prev.val;
    }

    public int peekMax() {
        return map.lastKey();
    }

    public int popMax() {
        Map.Entry<Integer, List<Node>> entry = map.lastEntry();
        List<Node> list = entry.getValue();
        removeFromList(list.get(list.size()-1));
        list.remove(list.size()-1);
        if (list.size() == 0) {
            map.remove(entry.getKey());
        } else {
            map.put(entry.getKey(), list);
        }
        return entry.getKey();
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */
