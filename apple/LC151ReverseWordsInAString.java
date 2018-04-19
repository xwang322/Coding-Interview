public class Solution {
    public String reverseWords(String s) {
        String[] s_list = s.trim().split("\\s+");
        String answer = "";
        for (int i = s_list.length-1; i >= 0; i--) {
            answer += s_list[i] + " ";
        }
        return answer.trim();
    }
}
