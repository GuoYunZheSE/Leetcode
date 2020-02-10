//
// Created by 郭蕴喆 on 2020/2/10.
//

#include "3.h"
#include "gtest/gtest.h"

using namespace std;

TEST(Longest_Substring_Without_Repeating_Characters,t1){
    Solution s;
    string sr="abcabcbb";
    EXPECT_EQ(3,s.lengthOfLongestSubstring(sr));
}
TEST(Longest_Substring_Without_Repeating_Characters,t2){
    Solution s;
    string sr="bbbbb";
    EXPECT_EQ(1,s.lengthOfLongestSubstring(sr));
}
TEST(Longest_Substring_Without_Repeating_Characters,t3){
    Solution s;
    string sr="pwwkew";
    EXPECT_EQ(3,s.lengthOfLongestSubstring(sr));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
