//
// Created by 郭蕴喆 on 2020/1/29.
//

#include "1.h"
#include "gtest/gtest.h"
using namespace std;


TEST(TS,t1){
    Solution s;
    vector<int> nums({3,2,4});
    int target=6;
    EXPECT_EQ(vector<int> ({1,2}),s.twoSum(nums,target));
}
TEST(TS,t2){
    Solution s;
    vector<int> nums({3,3});
    int target=6;
    EXPECT_EQ(vector<int> ({0,1}),s.twoSum(nums,target));
}
TEST(TS,t3){
    Solution s;
    vector<int> nums({3,2,3});
    int target=6;
    EXPECT_EQ(vector<int> ({0,2}),s.twoSum(nums,target));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}