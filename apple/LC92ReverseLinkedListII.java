/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;
        ListNode prev = null;
        for (int i = 0; i < m; i++) {
            prev = curr;
            curr = curr.next;
        }
        ListNode curr1 = curr;
        ListNode prev1 = prev;
        ListNode head2;
        for (int i = m; i <= n; i++) {
            head2 = curr1.next;
            curr1.next = prev1;
            prev1 = curr1;
            curr1 = head2;
        }
        prev.next = prev1;
        curr.next = curr1;
        return dummy.next;
    }
}
