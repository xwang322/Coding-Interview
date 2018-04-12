class Solution {
    /*
    public boolean detectCapitalUse(String word) {
        return word.equals(word.toUpperCase()) || word.equals(word.toLowerCase()) || Character.isUpperCase(word.charAt(0)) && word.substring(1).equals(word.substring(1).toLowerCase());
    }
    */
    public boolean detectCapitalUse(String word) {
        int numUp = 0;
        for (int i = 0; i < word.length(); i++) {
            if (Character.isUpperCase(word.charAt(i))) numUp++;
        }
        if (numUp == 1) return Character.isUpperCase(word.charAt(0));
        return numUp == 0 || numUp == word.length();
    }
}