public class Solution {
    public String reverseWords(String s) {
        Scanner parts = new Scanner(s);
        String answer = "";
        while (parts.hasNext()) {
            answer = parts.next() + " " + answer;
        }
        return answer.trim();
    }
}