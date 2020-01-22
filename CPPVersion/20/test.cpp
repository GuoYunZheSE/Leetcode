//
// Created by 郭蕴喆 on 2020/1/21.
//

#include "20.h"
#include <gtest/gtest.h>
using namespace std;

TEST(VP,t1) {
    Solution sol;
    bool res = sol.isValid("()");
    EXPECT_EQ(true, res);
}
TEST(VP,t2){
    Solution sol;
    bool res=sol.isValid("()[]{}");
    EXPECT_EQ(true,res);
}
TEST(VP,t3){
    Solution sol;
    bool res=sol.isValid("(]");
    EXPECT_EQ(false,res);
}
TEST(VP,t4){
    Solution sol;
    bool res=sol.isValid("([)]");
    EXPECT_EQ(false,res);
}
TEST(VP,t5){
    Solution sol;
    bool res=sol.isValid("{[]}");
    EXPECT_EQ(true,res);
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}