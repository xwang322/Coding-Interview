/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    // hashmap method, O(N) space and O(N) time
    public RandomListNode copyRandomList(RandomListNode head) {
        Map<RandomListNode, RandomListNode> hm = new HashMap<>();
        RandomListNode current = head;
        while (current != null) {
            hm.put(current, new RandomListNode(current.label));
            current = current.next;
        }
        current = head;
        while (current != null) {
            hm.get(current).next = hm.get(current.next);
            hm.get(current).random = hm.get(current.random);
            current = current.next;
        }
        return hm.get(head);
    }
}


public class Solution {
    // O(1) space and O(n) time
    public RandomListNode copyRandomList(RandomListNode head) {
        RandomListNode current = head;
        RandomListNode temp;
        while (current != null) {
            temp = current.next;
            RandomListNode copy = new RandomListNode(current.label);
            current.next = copy;
            copy.next = temp;
            current = temp;
        }
        current = head;
        while (current != null) {
            if (current.random != null) {
                current.next.random = current.random.next;
            }
            current = current.next.next;
        }
        current = head;
        RandomListNode dummy = new RandomListNode(0);
        RandomListNode dummycopy = dummy;
        RandomListNode copy;
        while (current != null) {
            temp = current.next.next;
            copy = current.next;
            dummycopy.next = copy;
            dummycopy = copy;
            current.next = temp;
            current = temp;
        }
        return dummy.next;
    }
}
