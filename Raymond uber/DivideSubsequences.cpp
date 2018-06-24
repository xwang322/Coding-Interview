/*
output the number of consecutive subsequenences whose sum is divisible by k
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
	int divideByK(vector<int>& nums, int k){
		vector<int>count(k, 0);
		vector<int>sum(nums.size()+1, 0);
		long res=0;
		count[0]=1;

		for(int i=1; i <= nums.size(); i++){
			
				sum[i]=(sum[i-1] + nums[i-1])%k;
			count[sum[i]]++;
		}

		for(int i=0; i < k ;i++){
			res+= (count[i] * (count[i]-1)/2);
		}
		
		return res;
	}
	
};
int main()
{
	
	Solution s;
	vector<int>nums={1,2,1,2,1,2};
	int k=2;
	cout << s.divideByK(nums, k);
	

	return 0;
}