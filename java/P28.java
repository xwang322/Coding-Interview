class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack == null) return -1;
        if (needle == null) return 0;
        int l1 = haystack.length();
        int l2 = needle.length();
        if (l1 < l2) return -1;
        int diff = l1-l2;
        for (int i = 0; i <= diff; i++) {
            if (haystack.substring(i, i+l2).equals(needle)) {
                return i;
            }
        }
        return -1;
    }
}