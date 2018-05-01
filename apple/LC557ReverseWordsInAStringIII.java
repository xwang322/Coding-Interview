class Solution {
    public String reverseWords(String s) {
        String[] temp = s.split(" ");
        for (int i = 0; i < temp.length; i++) {
            temp[i] = new StringBuilder(temp[i]).reverse().toString();
        }
        StringBuilder sb = new StringBuilder();
        for (String str : temp) {
            sb.append(str + " ");
        }
        return sb.toString().trim();
    }
}
