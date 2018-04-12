class Solution {
    public int compareVersion(String version1, String version2) {
        String[] version1_list = version1.split("\\.");
        String[] version2_list = version2.split("\\.");
        int maxlen = Math.max(version1_list.length, version2_list.length);
        for (int i = 0; i < maxlen; i++) {
            int v1_tok = 0;
            if (i < version1_list.length) {
                v1_tok = Integer.parseInt(version1_list[i]);
            }
            int v2_tok = 0;
            if (i < version2_list.length) {
                v2_tok = Integer.parseInt(version2_list[i]);
            }
            if (v1_tok < v2_tok)
                return -1;
            if (v1_tok > v2_tok)
                return 1;
        }
        return 0;
    }
}