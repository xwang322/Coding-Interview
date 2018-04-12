class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int l1 = s1.length();
        int l2 = s2.length();
        if (l1 > l2) return false;
        int[] count1 = new int[26];
        for (int i = 0; i < l1; i++) {
            count1[s1.charAt(i)-'a']++;
        }
        int[] count2 = new int[26];
        for (int i = 0; i < l2; i++) {
            count2[s2.charAt(i)-'a']++;
            if (i >= l1) count2[s2.charAt(i-l1)-'a']--;
            if (Arrays.equals(count1, count2)) return true;
        }
        return false;
    }
}
