//
// Created by 郭蕴喆 on 2020/2/10.
//

#include "1248.h"
#include "gtest/gtest.h"

using namespace std;

TEST(Count_Number_of_Nice_Subarrays,t1){
    Solution s;
    vector<int> nums({1,1,2,1,1});
    int target=3;
    EXPECT_EQ(2,s.numberOfSubarrays(nums,target));
}
TEST(Count_Number_of_Nice_Subarrays,t2){
    Solution s;
    vector<int> nums({2,4,6});
    int target=1;
    EXPECT_EQ(0,s.numberOfSubarrays(nums,target));
}
TEST(Count_Number_of_Nice_Subarrays,t3){
    Solution s;
    vector<int> nums({2,2,2,1,2,2,1,2,2,2});
    int target=2;
    EXPECT_EQ(16,s.numberOfSubarrays(nums,target));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
