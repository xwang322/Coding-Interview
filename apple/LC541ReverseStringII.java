class Solution {
    public String reverseStr(String s, int k) {
        if (s == null || s.length() == 0) return s;
        char[] temp = s.toCharArray();
        int length = temp.length - 1;
        int i = 0;
        while (i <= length) {
            int j = Math.min(i+k-1, length);
            swap(temp, i, j);
            i += 2*k;
        }
        return new String(temp);
    }

    public void swap(char[] temp, int i, int j) {
        while (i < j) {
            char c = temp[i];
            temp[i] = temp[j];
            temp[j] = c;
            i++;
            j--;
        }
    }
}
