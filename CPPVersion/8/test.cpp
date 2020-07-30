//
// Created by 郭蕴喆 on 2020/7/31.
//

#include <gtest/gtest.h>
#include "8.h"

using namespace std;

TEST(atoi,t1){
    Solution s;
    EXPECT_EQ(42,s.myAtoi("2147483646"));
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}