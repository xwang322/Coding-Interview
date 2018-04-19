/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        if(intervals.size() == 0 || intervals.size() == 1) return intervals;
        intervals.sort((i1, i2) -> Integer.compare(i1.start, i2.start));
        List<Interval> answer = new ArrayList<>();
        for (Interval interval : intervals) {
            if (answer.size() != 0 && answer.get(answer.size()-1).end >= interval.start) {
                int start = answer.get(answer.size()-1).start;
                int end = Math.max(answer.get(answer.size()-1).end, interval.end);
                answer.remove(answer.size()-1);
                answer.add(new Interval(start, end));
            } else {
                answer.add(interval);
            }
        }
        return answer;
    }
}
