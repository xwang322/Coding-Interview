class Solution {
    public int maxProduct(String[] words) {
        int[] chars = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            int num = 0;
            for (int j = 0; j < words[i].length(); j++) {
                num |= 1<<(words[i].charAt(j)-'a');
            }
            chars[i] = num;
        }
        int answer = 0;
        for (int i = 0; i < words.length; i++) {
            for (int j = i+1; j < words.length; j++) {
                if ((chars[i]&chars[j]) == 0) {
                    answer = Math.max(answer, words[i].length()*words[j].length());
                }
            }
        }
        return answer;
    }
}