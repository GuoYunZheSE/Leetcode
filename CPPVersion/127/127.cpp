//
// Created by 郭蕴喆 on 2021/4/12.
//

#include <gtest/gtest.h>
#include "127.h"

using namespace std;

TEST(SWM,t1){
    string beginWord = "hit";
    string endWord = "cog";
    vector <string> wordList ({"hot","dot","tog","cog"});
    Solution S;
    EXPECT_EQ(5,S.ladderLength(beginWord,endWord,wordList));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
