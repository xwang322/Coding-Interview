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
        Collections.sort(intervals, new Comparator<Interval>() {
            public int compare(Interval obj0, Interval obj1) {
                return obj0.start - obj1.start;
            }
        });
        List<Interval> answer = new ArrayList<>();
        Interval prev = null;
        for (Interval inter:intervals) {
            if (prev == null || inter.start > prev.end) {
                answer.add(inter);
                prev = inter;
            }
            else if (prev.end < inter.end){
                prev.end = inter.end;
            }
        }
        return answer;
    }
}
