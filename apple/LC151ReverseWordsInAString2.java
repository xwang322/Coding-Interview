public class Solution {
    public String reverseWords(String s) {
        if (s == null || s.trim().equals("")) return s.trim();
        String[] temp = s.split(" ");
        int length = temp.length;
        StringBuilder sb = new StringBuilder();
        for (String str : temp) {
            str = str.replace(" ", "");
            str = str.trim();
            if (str.equals("")) continue;
            StringBuilder temp1 = new StringBuilder(str);
            sb.append(temp1.reverse());
            sb.append(" ");
        }
        int index = sb.toString().lastIndexOf(" ");
        sb.replace(index, sb.length(), ""); // string.replace(sequence of string, replacement), sequence of string here is two indices
        return sb.reverse().toString();
    }
}
