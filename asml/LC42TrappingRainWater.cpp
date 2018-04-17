class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0) return 0;
        vector<int> left(height.size());
        vector<int> right(height.size());
        int leftmost = 0;
        for (int i = 0; i < height.size(); i++) {
            if (height[i] > leftmost) {
                leftmost = height[i];
            }
            left[i] = leftmost;
        }
        int rightmost = 0;
        for (int i = height.size()-1; i >= 0; i--) {
            if (height[i] > rightmost) {
                rightmost = height[i];
            }
            right[i] = rightmost;
        }
        int answer = 0;
        for (int i = 0; i < height.size(); i++) {
            if (min(right[i], left[i]) > height[i]) {
                answer += min(left[i], right[i])-height[i];
            }
        }
        return answer;
    }
};
