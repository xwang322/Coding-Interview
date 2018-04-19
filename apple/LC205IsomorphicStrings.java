class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s == null || t== null) return s==t;
        HashMap<Character, Character> hm = new HashMap<Character, Character>();
        for (int i=0; i < s.length(); i++) {
            char a = s.charAt(i);
            char b = t.charAt(i);
            if (hm.containsKey(a)) {
                if (!hm.get(a).equals(b)) return false;
                else continue;
            } else {
                if(!hm.containsValue(b)) hm.put(a,b);
                else return false;
            }
        }
        return true;
    }
}
