class Solution {
    public int longestValidParentheses(String s) {
        if(s == null || s.length() == 0) return 0;
        Stack<Integer> stack = new Stack<>();
        int answer = 0;
        int flag = -1;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                if (flag == -1) {
                    stack.push(i);
                } else {
                    stack.push(flag);
                    flag = -1;
                }
            } else {
                if (stack.isEmpty()) {
                    flag = -1;
                } else {
                    int temp = stack.pop();
                    answer = Math.max(answer, i-temp+1);
                    flag = temp;
                }
            }
        }
        return answer;
    }
}
