class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) return 0;
        int answer = 0;
        int start = 0;
        int i = 0;
        Map<Character, Integer> hm = new HashMap<>();
        while (i < s.length()) {
            if (hm.containsKey(s.charAt(i))) {
                start = Math.max(start, hm.get(s.charAt(i))+1);
            }
            answer = Math.max(answer, i-start+1);
            hm.put(s.charAt(i), i);
            i++;
        }
        return answer;
    }
}
