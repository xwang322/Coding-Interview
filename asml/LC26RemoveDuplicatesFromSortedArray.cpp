class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int start = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[start]) {
                nums[start+1] = nums[i];
                start++;
            }
        }
        return start+1;
    }
};
