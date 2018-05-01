class Solution {
    // use hashmap solution
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hm = new HashMap<>();
        int[] answer = new int[2];
        for (int i = 0; i < nums.length; i++) {
            if (!hm.containsKey(target-nums[i])) {
                hm.put(nums[i], i);
            } else {
                answer[0] = i;
                answer[1] = hm.get(target-nums[i]);
                return answer;
            }
        }
        return answer;
    }
}

class Solution {
    // O(nlogn) method, sort first and then find the original index
    public int[] twoSum(int[] nums, int target) {
        int[] nums2 = Arrays.copyOf(nums, nums.length);
        Arrays.sort(nums2);
        int i = 0;
        int j = nums2.length-1;
        int[] temp = new int[2];
        while (i < j) {
            if (nums2[i] + nums2[j] == target) {
                temp[0] = nums2[i];
                temp[1] = nums2[j];
                break;
            } else if (nums2[i] + nums2[j] > target) {
                j--;
            } else {
                i++;
            }
        }
        int[] answer = new int[2];
        for (int k = 0; k < nums.length; k++) {
            if (nums[k] == temp[0]) {
                answer[0] = k;
                break;
            }
        }
        if (temp[0] == temp[1]) {
            for (int k = 0; k < nums.length; k++) {
                if (nums[k] == temp[1] && k != answer[0]) {
                    answer[1] = k;
                    return answer;
                }
            }
        } else {
            for (int k = 0; k < nums.length; k++) {
                if (nums[k] == temp[1]) {
                    answer[1] = k;
                    return answer;
                }
            }
        }
        return answer;
    }
}
