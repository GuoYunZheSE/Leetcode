//
// Created by 郭蕴喆 on 2019/12/10.
//

#include <gtest/gtest.h>
#include <iostream>
#include "441.h"

TEST(Arranging_Coins,t1){
    Solution s;
    EXPECT_EQ(3,s.arrangeCoins(8));
}

TEST(Arranging_Coins,t2){
    Solution s;
    EXPECT_EQ(
            60070,s.arrangeCoins(1804289383));
}

int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}