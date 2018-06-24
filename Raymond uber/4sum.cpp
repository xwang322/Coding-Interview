#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
	void sum(vector<int>&nums, int target){
		if(nums.size() < 4)return;

		sort(nums.begin(), nums.end());

		for(int i=0; i < nums.size()-3; i++){
			if(i>0 && nums[i]==nums[i-1])continue;
			for(int j=i+1; j < nums.size()-2; j++){
				if(j> i+1 && nums[j]==nums[j-1])continue;
				int left=j+1, right=nums.size()-1;
				while(left < right){
					int sum=nums[left] + nums[right] + nums[i] + nums[j];
					if(sum==target){
						left++;
						right--;
						while(left < right && nums[left]==nums[left-1])left++;
                        while(left < right && nums[right]==nums[right+1])right--;
					}
					else if(sum < target)left++;
					else right--;
				}
			}
		}
	}
    
};
int main()
{
	
	Solution s;
	vector<int>nums={1, 0, -1, 0, -2, 2};
	s.sum(nums, 0);

	return 0;
}