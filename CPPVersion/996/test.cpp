//
// Created by 郭蕴喆 on 2020/2/25.
//

#include "996.h"
#include "gtest/gtest.h"

using namespace std;

TEST(numSquarefulPerms,t1){
    Solution s;
    vector<int> nums({2,2,2});
    EXPECT_EQ(1,(s.numSquarefulPerms(nums)));
}
TEST(numSquarefulPerms,t2){
    Solution s;
    vector<int> nums({1,17,8});
    EXPECT_EQ(2,(s.numSquarefulPerms(nums)));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
