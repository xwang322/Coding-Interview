class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2) return nums.size();
        int rear = 1;
        for(int i = 2; i < nums.size(); i++) {
            if (nums[i] != nums[rear-1]) {
                nums[++rear] = nums[i];
            }
        }
        return rear+1;
    }
};
