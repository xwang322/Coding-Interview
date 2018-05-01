class Solution {
    public int calculate(String s) {
        if (s == null || s.length() == 0) return 0;
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        int sign = 1;
        int i = 0;
        while (i <= s.length()-1) {
            if (Character.isDigit(s.charAt(i))) {
                int num = s.charAt(i) - '0';
                while (i+1 <= s.length()-1 && Character.isDigit(s.charAt(i+1))) {
                    num = num * 10 + s.charAt(i+1) - '0';
                    i++;
                }
                answer += sign*num;
            } else if (s.charAt(i) == '+') {
                sign = 1;
            } else if (s.charAt(i) == '-') {
                sign = -1;
            } else if (s.charAt(i) == '(') {
                stack.push(answer);
                stack.push(sign);
                answer = 0;
                sign = 1;
            } else if (s.charAt(i) == ')') {
                answer = answer * stack.pop() + stack.pop();
            }
            i++;
        }
        return answer;
    }
}
