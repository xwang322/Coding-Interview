class Solution {
    public String reverseString(String s) {
        if (s==null) return s;
        char[] array = s.toCharArray();
        for (int i = 0, j = array.length-1; i <= j; i++, j--) {
            char temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
        return new String(array);
    }
}
