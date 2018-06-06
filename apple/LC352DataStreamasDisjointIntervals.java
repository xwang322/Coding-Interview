/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class SummaryRanges {
    List<Interval> array;
    public SummaryRanges() {
        array = new ArrayList<>();
    }
    public void addNum(int val) {
        int left = 0;
        int right = array.size()-1;
        while (left <= right) {
            int mid = (right-left)/2 + left;
            Interval interval = array.get(mid);
            if (interval.start <= val && val <= interval.end) {
                return;
            } else if (interval.start > val) {
                right = mid-1;
            } else {
                left = mid+1;
            }
        }
        int position = Math.min(left, right)+1;
        array.add(position, new Interval(val, val));
        if (position+1 < array.size() && val == array.get(position+1).start-1) {
            array.get(position).end = array.get(position+1).end;
            array.remove(position+1);
        } 
        if (position-1 >= 0 && val == array.get(position-1).end+1) {
            array.get(position).start = array.get(position-1).start;
            array.remove(position-1);
        }
    }
    public List<Interval> getIntervals() {
        return array;
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * List<Interval> param_2 = obj.getIntervals();
 */