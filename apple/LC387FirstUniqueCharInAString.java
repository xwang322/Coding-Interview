// typical solution use 2 pass to find the first unique character
class Solution {
    public int firstUniqChar(String s) {
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i)-'a']++;
        }
        for (int i = 0; i < s.length(); i++) {
            if (freq[s.charAt(i)-'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
}

// LinkedHashMap is like OrderedDict in Python, this will only need one pass
class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> hm = new LinkedHashMap<>();
        Set<Character> set = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            if (set.contains(s.charAt(i))) {
                if (hm.get(s.charAt(i)) != null) {
                    hm.remove(s.charAt(i));
                }
            } else {
                set.add(s.charAt(i));
                hm.put(s.charAt(i), i);
            }
        }
        return hm.size() == 0 ? -1 : hm.entrySet().iterator().next().getValue();
    }
}
