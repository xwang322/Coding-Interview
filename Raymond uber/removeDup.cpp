/*
1.Given a sorted linked list, delete all duplicates such that each element appear only once.
2. Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.
*/
/*
merge two sorted lists
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null) {
            return head;
        }
        ListNode dummy = new ListNode(0);
        ListNode prev = null;
        ListNode node = dummy;
        while(head!=null) {
            if((prev==null || prev.val != head.val) && (head.next == null ||head.val!=head.next.val)) {
                node.next = head;
                node = node.next;
            }
            prev = head;
            head = head.next;
            node.next = null;
            
        }
        return dummy.next;
    }
}