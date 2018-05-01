//第二题是3个有序的列表，从里面分别取出3个数字，a,b,c， 要求找到最小的范围，就是max(abc) - min(abc)最小，lc上有类似的两个列表的题。
import java.util.*;
import java.io.*;
class Element {
    int val;
    int row;
    int index;
    Element (int v, int r, int i) {
        this.val = v;
        this.row = r;
        this.index = i;
    }
}
class Solution {
    public static void main(String[] args) {
        List<List<Integer>> question = Arrays.asList(Arrays.asList(4, 10, 15, 24, 26), Arrays.asList(0, 9, 12, 20), Arrays.asList(5, 18, 22, 30));
        int[] answer = FindRange(question);
        for (Integer each : answer) {
            System.out.println(each);
        }
    }

    public static int[] FindRange(List<List<Integer>> ranges) {
        if (ranges == null || ranges.size() == 0) return null;
        if (ranges.size() == 1) return new int[]{ranges.get(0).get(0), ranges.get(0).get(0)};
        Queue<Element> pq = new PriorityQueue<Element>(new Comparator<Element>(){
            @Override
            public int compare(Element a, Element b) {
                return a.val - b.val;
            }
        });
        int max = Integer.MIN_VALUE;
        int start = -1;
        int end = -1;
        int range = Integer.MAX_VALUE;
        int[] answer = new int[ranges.size()];
        for (int i = 0; i < ranges.size(); i++) {
            Element ele = new Element(ranges.get(i).get(0), i, 0);
            pq.offer(ele);
            max = Math.max(max, ele.val);
        }
        while (pq.size() == ranges.size()) {
            Element curr = pq.poll();
            if (max-curr.val < range) {
                range = max-curr.val;
                start = curr.val;
                end = max;
                answer[0] = curr.val;
                int j = 1;
                for (Element ele : pq.toArray(new Element[ranges.size()-1])) {
                    answer[j++] = ele.val;
                }
            }
            if (curr.index+1 <= ranges.get(curr.row).size()-1) {
                Element next = new Element(ranges.get(curr.row).get(curr.index+1), curr.row, curr.index+1);
                pq.offer(next);
                if (next.val > max) {
                    max = next.val;
                }
            }
        }
    return answer;
    }
}
