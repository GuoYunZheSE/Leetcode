//
// Created by 郭蕴喆 on 2020/1/19.
//

#include "65.h"
#include <gtest/gtest.h>
using namespace std;

TEST(VN,t1){
    string s=" -90e3   ";
    Solution sol;
    bool res=sol.isNumber(s);
    EXPECT_EQ(true,res);
}
TEST(VN,t2){
    string s="1 a";
    Solution sol;
    bool res=sol.isNumber(s);
    EXPECT_EQ(false,res);
}
TEST(VN,t3){
    string s=" 005047e+6";
    Solution sol;
    bool res=sol.isNumber(s);
    EXPECT_EQ(true,res);
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}