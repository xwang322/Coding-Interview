class Solution {
    public int calculate(String s) {
        if (s == null) return 0;
        char sign = '+';
        Stack<Integer> stack = new Stack<>();
        int i = 0;
        int num = 0;
        while (i <= s.length()-1) {
            if (Character.isDigit(s.charAt(i))) {
                num = s.charAt(i) - '0';
                while (i+1 <= s.length()-1 && Character.isDigit(s.charAt(i+1))) {
                    num = num * 10 + s.charAt(i+1) - '0';
                    i++;
                }
            }
            if ((s.charAt(i) != ' ' && !Character.isDigit(s.charAt(i))) || i == s.length()-1) {
                if (sign == '+') {
                    stack.push(num);
                } else if (sign == '-') {
                    stack.push(-num);
                } else if (sign == '*') {
                    stack.push(stack.pop()*num);
                } else if (sign == '/') {
                    stack.push(stack.pop()/num);
                }
                sign = s.charAt(i);
                num = 0;
            }
            i++;
        }
        int answer = 0;
        while (stack.size() > 0) {
            answer += stack.pop();
        }
        return answer;
    }
}
