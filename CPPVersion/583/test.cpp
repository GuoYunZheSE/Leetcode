//
// Created by 郭蕴喆 on 2020/2/12.
//

#include "583.h"
#include "gtest/gtest.h"

using namespace std;

TEST( Delete_Operation_for_Two_Strings,t1){
    Solution s;
    string word1="sea";
    string word2="eat";
    EXPECT_EQ(2,s.minDistance(word1,word2));
}
TEST( Delete_Operation_for_Two_Strings,t2){
    Solution s;
    string word1="abcdaf";
    string word2="acbcf";
    EXPECT_EQ(3,s.minDistance(word1,word2));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
