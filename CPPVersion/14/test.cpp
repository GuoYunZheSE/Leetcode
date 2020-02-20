//
// Created by 郭蕴喆 on 2020/2/21.
//

#include <gtest/gtest.h>
#include "14.h"

using namespace std;

TEST(Longest_Common_Prefix,t1){
    vector<string> strs({"flower","flow","flight"});
    Solution s;
    EXPECT_EQ("fl",s.longestCommonPrefix(strs));
}
TEST(Longest_Common_Prefix,t2){
    vector<string> strs({"dog","racecar","car"});
    Solution s;
    EXPECT_EQ("",s.longestCommonPrefix(strs));
}
TEST(Longest_Common_Prefix,t3){
    vector<string> strs({"aa","a"});
    Solution s;
    EXPECT_EQ("a",s.longestCommonPrefix(strs));
}
TEST(Longest_Common_Prefix,t4){
    vector<string> strs({"a","b"});
    Solution s;
    EXPECT_EQ("",s.longestCommonPrefix(strs));
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}