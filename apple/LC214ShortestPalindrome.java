class Solution {
    public String shortestPalindrome(String s) {
        if (s == null || s.length() == 0) return s;
        StringBuilder sb1 = new StringBuilder();
        sb1.append(s);
        String r = sb1.reverse().toString();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < r.length()+1; i++) {
            if (s.startsWith(r.substring(i))) {
                sb.append(r.substring(0, i));
                sb.append(s);
                return sb.toString();
            }
        }
        return sb.toString();
    }
}
