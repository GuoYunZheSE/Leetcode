//
// Created by 郭蕴喆 on 2020/2/27.
//

#include "862.h"
#include "gtest/gtest.h"

using namespace std;

TEST(shortestSubarray,t1){
    Solution s;
    vector<int> nums({1});
    EXPECT_EQ(1,s.shortestSubarray(nums,1));
}
TEST(shortestSubarray,t2){
    Solution s;
    vector<int> nums({1,2});
    EXPECT_EQ(-1,s.shortestSubarray(nums,4));
}
TEST(shortestSubarray,t3){
    Solution s;
    vector<int> nums({2,-1,2});
    EXPECT_EQ(3,s.shortestSubarray(nums,3));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}