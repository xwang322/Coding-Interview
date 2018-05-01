//BST变成顺序双向链表，要写recursion，方法是每次返回最左边和最右边的节
import java.util.*;
import java.io.*;
class ListNode {
    int val;
    ListNode prev;
    ListNode next;
    ListNode (int val) {
        this.val = val;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
        this.val = x;
    }
}

class Solution {
    public static void main(String[] args) {
        TreeNode t1 = new TreeNode(0);
        TreeNode t2 = new TreeNode(-3);
        TreeNode t3 = new TreeNode(-10);
        TreeNode t4 = new TreeNode(5);
        TreeNode t5 = new TreeNode(9);
        t1.left = t2;
        t1.right = t5;
        t2.left = t3;
        t5.left = t4;
        ListNode head = BSTtoLL(t1);
        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }

    public static ListNode BSTtoLL(TreeNode root) {
        if (root == null) return null;
        Queue<TreeNode> queue = new LinkedList<>();
        Map<TreeNode, ListNode> hm = new HashMap<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int count = queue.size();
            for (int i = 0; i < count; i++) {
                TreeNode treenode = queue.poll();
                ListNode node = new ListNode(treenode.val);
                hm.put(treenode, node);
                if (treenode.left != null) queue.offer(treenode.left);
                if (treenode.right != null) queue.offer(treenode.right);
                if (findPrev(treenode) != null) {
                    node.prev = new ListNode(findPrev(treenode).val);
                } else {
                    node.prev = new ListNode(Integer.MIN_VALUE);
                }
                if (findNext(treenode) != null) {
                    node.next = new ListNode(findNext(treenode).val);
                } else {
                    node.next = new ListNode(Integer.MAX_VALUE);
                }
            }
        }
        TreeNode dummy = root;
        while (dummy.left != null) {
            dummy = dummy.left;
        }
        ListNode first = hm.get(dummy);
        for (TreeNode temp : hm.keySet()) {
            System.out.println(temp.val);
            System.out.println(hm.get(temp).val);
            System.out.println(hm.get(temp).prev.val);
            System.out.println(hm.get(temp).next.val);
        }
        return first;
    }

    public static TreeNode findPrev(TreeNode root) {
        if (root == null || root.left == null) return null;
        root = root.left;
        while (root.right != null) {
            root = root.right;
        }
        return root;
    }
    public static TreeNode findNext(TreeNode root) {
        if (root == null || root.right == null) return null;
        root = root.right;
        while (root.left != null) {
            root = root.left;
        }
        return root;
    }
}
