class MaxStack {
    class Node {
        int value;
        boolean valid;
        int index;
        Node (int v, boolean vl, int i) {
            this.value = v;
            this.valid = vl;
            this.index = i;
        }
    }

    Queue<Node> pq;
    List<Node> list;
    public MaxStack() {
        list = new ArrayList<>();
        pq = new PriorityQueue<>((x1, x2)->(x2.value != x1.value ? x2.value-x1.value : x2.index-x1.index));
    }

    public void push(int x) {
        Node node = new Node(x, true, list.size());
        pq.offer(node);
        list.add(node);
    }

    public int pop() {
        while (list.size()>0 && !list.get(list.size()-1).valid) list.remove(list.size()-1);
        Node node = list.remove(list.size()-1);
        pq.remove(node);
        return node.value;
    }

    public int top() {
        while (list.size()>0 && !list.get(list.size()-1).valid) list.remove(list.size()-1);
        return list.get(list.size()-1).value;
    }

    public int peekMax() {
        return pq.peek().value;
    }

    public int popMax() {
        Node node = pq.poll();
        node.valid = false;
        return node.value;
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
