class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        List<List<String>> answer = new ArrayList<>();
        if (strings == null || strings.length == 0) return answer;
        Map<String, List<String>> hm = new HashMap<>();
        for (String str : strings) {
            int shift = str.charAt(0) - 'a';
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < str.length(); i++) {
                sb.append((str.charAt(i)+26-shift)%26);
            }
            if (!hm.containsKey(sb.toString())) {
                hm.put(sb.toString(), new ArrayList<String>());

            }
            hm.get(sb.toString()).add(str);
        }
        return new ArrayList<List<String>>(hm.values());
    }
}
