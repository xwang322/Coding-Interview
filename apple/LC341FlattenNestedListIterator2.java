/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {
    List<Integer> answer;
    int current = 0;

    public NestedIterator(List<NestedInteger> nestedList) {
        answer = new ArrayList<>();
        helper(nestedList);

    }

    public void helper(List<NestedInteger> nestedList) {
        for (NestedInteger element : nestedList) {
            if (element.isInteger()) {
                answer.add(element.getInteger());
            } else {
                helper(element.getList());
            }
        }
    }

    @Override
    public Integer next() {
        int number = answer.get(current);
        current++;
        return number;
    }

    @Override
    public boolean hasNext() {
        if (current == answer.size()) return false;
        else return true;
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
