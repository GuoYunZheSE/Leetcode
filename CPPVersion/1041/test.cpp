//
// Created by 郭蕴喆 on 2020/2/3.
//

#include <gtest/gtest.h>
#include "1041.h"

using namespace std;

TEST(RBiC,t1){
    string ins="GGLLGG";
    Solution s;
    EXPECT_TRUE(s.isRobotBounded(ins));
}
TEST(RBiC,t2){
    string ins="GG";
    Solution s;
    EXPECT_FALSE(s.isRobotBounded(ins));
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}