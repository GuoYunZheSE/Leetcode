#include <string.h>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
	int pivotIndex(vector<int>& nums) {
		int size = nums.size();
		if (size == 0) {
			return -1;
		}
		if (size == 1) {
			return 0;
		}
		else
		{
			int sum = 0;
			int sum_left = 0;
			for (int i = 0; i < size; i++) {
				sum += nums[i];
			}
			int sum_right = sum;
			for (int pivot = 0; pivot < size; pivot++) {
				sum_right -= nums[pivot];
				if (sum_right == sum_left) {
					return pivot;
				}
				sum_left += nums[pivot];
			}
			return -1;
		}
	}
};

int main() {
	Solution s;
	vector<int> nums;
	s.pivotIndex(nums);
	return 0;
}