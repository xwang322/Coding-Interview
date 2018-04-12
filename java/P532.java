class Solution {
    public int findPairs(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k < 0) return 0;
        Map<Integer, Integer> maps = new HashMap<>();
        for (int num:nums) {
            maps.put(num, maps.getOrDefault(num, 0)+1);
        }
        int count = 0;
        for (Map.Entry<Integer, Integer> entry:maps.entrySet()) {
            if (k == 0){
                if (entry.getValue() >= 2){
                    count++;
                }
            }
            else {
                if (maps.containsKey(entry.getKey()+k)) {
                    count++;
                }
            }
        }
        return count;
    }
}