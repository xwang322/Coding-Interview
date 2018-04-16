class Solution {
    public boolean isAnagram(String s, String t) {
        int[] dictionary = new int[26];
        for (int i = 0; i < s.length(); i++) dictionary[s.charAt(i)-'a']++;
        for (int i = 0; i < t.length(); i++) dictionary[t.charAt(i)-'a']--;
        for (int item : dictionary){
            if (item != 0) {
                return false;
            }
        }
        return true;
    }
}
