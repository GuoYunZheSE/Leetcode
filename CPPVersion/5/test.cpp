//
// Created by 郭蕴喆 on 2020/7/7.
//

#include "5.h"
#include "gtest/gtest.h"

using namespace std;

TEST(LPS,t1){
    Solution s;
    EXPECT_EQ("bb",s.longestPalindrome("cbbd"));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
