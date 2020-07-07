//
// Created by 郭蕴喆 on 2020/7/7.
//

#include "67.h"
#include "gtest/gtest.h"

using namespace std;

TEST(addBinary,t1){
    Solution s;
    string s1="11";
    string s2="1";
    EXPECT_EQ("100",s.addBinary(s1,s2));
}
TEST(addBinary,t2){
    Solution s;
    string s1="110";
    string s2="1";
    EXPECT_EQ("111",s.addBinary(s1,s2));
}
TEST(addBinary,t3){
    Solution s;
    string s1="111";
    string s2="1";
    EXPECT_EQ("1000",s.addBinary(s1,s2));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
