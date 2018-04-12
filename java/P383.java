class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c:magazine.toCharArray()) {
            int count = map.getOrDefault(c, 0)+1;
            map.put(c, count);
        }
        for (char c:ransomNote.toCharArray()) {
            int count = map.getOrDefault(c, 0)-1;
            if (count<0) return false;
            map.put(c, count);
        }
        return true;
    }
}