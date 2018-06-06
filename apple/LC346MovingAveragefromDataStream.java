class MovingAverage {
    Queue<Integer> queue;
    int size;
    int total;
    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        this.size = size;
        this.total = 0;
        this.queue = new LinkedList<>();
    }
    
    public double next(int val) {
        queue.offer(val);
        total += val;
        if (queue.size() > size) total -= queue.poll();
        return (double) total / (double) queue.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */