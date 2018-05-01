class Solution {
    public void reverseWords(char[] str) {
        int start = 0;
        for (int i = 0; i <= str.length; i++) {
            if (i == str.length || str[i] == ' ') {
                tempswap(str, start, i-1);
                start = i+1;
            }
        }
        tempswap(str, 0, str.length-1);
    }

    public void tempswap(char[] str, int i, int j) {
        while (i < j) {
            char c = str[i];
            str[i++] = str[j];
            str[j--] = c;
        }
    }
}
