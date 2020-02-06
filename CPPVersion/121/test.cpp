//
// Created by 郭蕴喆 on 2020/2/6.
//
#include "121.h"
#include "gtest/gtest.h"

using namespace std;

TEST(BTBSS,t1){
    Solution s;
    vector<int> nums({7,1,5,3,6,4});
    EXPECT_EQ(5,s.maxProfit(nums));
}
TEST(BTBSS,t2){
    Solution s;
    vector<int> nums({7,6,4,3,1});
    EXPECT_EQ(0,s.maxProfit(nums));
}
TEST(BTBSS,t3){
    Solution s;
    vector<int> nums({});
    EXPECT_EQ(0,s.maxProfit(nums));
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
