//
// Created by 郭蕴喆 on 2020/2/24.
//

#include "1358.h"
#include "gtest/gtest.h"

using namespace std;

TEST(Number_of_Substrings_Containing_All_Three_Characters,t1){
    Solution s;
    string str="abcabc";
    EXPECT_EQ(10,s.numberOfSubstrings(str));
}

TEST(Number_of_Substrings_Containing_All_Three_Characters,t2){
    Solution s;
    string str="aaacb";
    EXPECT_EQ(3,s.numberOfSubstrings(str));
}

TEST(Number_of_Substrings_Containing_All_Three_Characters,t3){
    Solution s;
    string str="abc";
    EXPECT_EQ(1,s.numberOfSubstrings(str));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}