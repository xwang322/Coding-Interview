/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        if(intervals == null || intervals.length == 0) {
            return 0;
        }
        Arrays.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval i1, Interval i2) {
                return i1.start - i2.start;
            }
        });
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        pq.offer(intervals[0].end);
        for(int i = 1; i < intervals.length; i++) {
            if(intervals[i].start >= pq.peek()) {
                pq.poll();
            }
            pq.offer(intervals[i].end);
        }
        return pq.size();
    }
}