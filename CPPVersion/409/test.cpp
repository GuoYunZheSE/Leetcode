//
// Created by 郭蕴喆 on 2019/12/13.
//
#include "409.h"
#include <gtest/gtest.h>

TEST(Longest_Palindrome,t1){
    Solution s;
    EXPECT_EQ(7,s.longestPalindrome("abccccdd"));
}

int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}