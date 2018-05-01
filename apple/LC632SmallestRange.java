class Solution {
    class Element {
        int val;
        int index;
        int number;
        public Element (int v, int i, int n) {
            this.val = v;
            this.index = i;
            this.number = n;
        }
    }
    public int[] smallestRange(List<List<Integer>> nums) {
        Queue<Element> pq = new PriorityQueue<Element>(new Comparator<Element>() {
            @Override
            public int compare(Element a, Element b) {
                return a.val - b.val;
            }
        });
        int max = Integer.MIN_VALUE;
        int start = -1;
        int end = -1;
        for (int i = 0; i < nums.size(); i++) {
            Element element = new Element(nums.get(i).get(0), i, 0);
            pq.offer(element);
            max = Math.max(max, nums.get(i).get(0));
        }
        int range = Integer.MAX_VALUE;
        while (pq.size() == nums.size()) {
            Element curr = pq.poll();
            if (max-curr.val < range) {
                range = max-curr.val;
                start = curr.val;
                end = max;
            }
            if (curr.number+1 <= nums.get(curr.index).size()-1) {
                Element next = new Element(nums.get(curr.index).get(curr.number+1), curr.index, curr.number+1);
                pq.offer(next);
                if (next.val > max) {
                    max = next.val;
                }
            }
        }
        return new int[]{start, end};
    }
}
