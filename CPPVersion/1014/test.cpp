//
// Created by 郭蕴喆 on 2020/2/6.
//

#include "1014.h"
#include "gtest/gtest.h"

using namespace std;

TEST(BTBSS,t1){
    Solution s;
    vector<int> nums({8,1,5,2,6});
    EXPECT_EQ(11,s.maxScoreSightseeingPair(nums));
}
TEST(BTBSS,t2){
    Solution s;
    vector<int> nums({1,2,2});
    EXPECT_EQ(3,s.maxScoreSightseeingPair(nums));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
