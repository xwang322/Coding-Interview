class Solution {
    public String convertToTitle(int n) {
        if (n <= 0) return "";
        StringBuffer answer = new StringBuffer();
        while (n>0) {
            answer.insert(0, (char)('A'+(n-1)%26));
            n = (n-1)/26;
        }
        return answer.toString();
    }
}