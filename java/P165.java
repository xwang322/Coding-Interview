class Solution {
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\.");
        String[] v2 = version2.split("\\.");
        // can use either larger length or shorter length to compare
        int length = Math.max(v1.length, v2.length);
        for (int i = 0; i < length; i++) {
            int l1 = i<v1.length? Integer.parseInt(v1[i]):0;
            int l2 = i<v2.length? Integer.parseInt(v2[i]):0;
            if (l1 > l2) return 1;
            else if (l1 < l2) return -1;
            else continue;
        }
        return 0;
    }
}