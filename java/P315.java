class Solution { 
    class TreeNode {
        TreeNode left;
        TreeNode right;
        int val;
        int count = 1;
        public TreeNode(int val) {
            this.val = val;
        }
    }
    // using BST for the first time
    public List<Integer> countSmaller(int[] nums) {
        ArrayList<Integer> answer = new ArrayList<>();
        if (nums == null || nums.length == 0) return answer;
        TreeNode root = new TreeNode(nums[nums.length-1]);
        answer.add(0);
        for (int i = nums.length-2; i >=0; i--) {
            int count = insertBST(root, nums[i]);
            answer.add(count);
        }
        Collections.reverse(answer);
        return answer;
    }
    
    public int insertBST(TreeNode node, int val) {
        int thiscount = 0;
        while(true) {
            if(val <= node.val) {
                node.count++;
                if (node.left == null) {
                    node.left = new TreeNode(val);
                    break;
                }
                else {
                    node = node.left;
                }
            }
            else {
                thiscount += node.count;
                if (node.right == null) {
                    node.right = new TreeNode(val);
                    break;
                }
                else {
                    node = node.right;
                }
            }
        }
        return thiscount;
    }
}