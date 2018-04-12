class Solution {
    public int hIndex(int[] citations) {
        int length = citations.length;
        if (citations == null || citations.length == 0) return 0;
        int[] counts = new int[length+1];
        for (int c:citations) {
            if (c > length) counts[length]++;
            else counts[c]++;
        }
        
        int answer = 0;
        for (int k = length; k>=0; k--) {
            answer += counts[k];
            if (answer>=k) return k;
        }
        return 0;
    }
}