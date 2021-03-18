//
// Created by 郭蕴喆 on 2021/3/18.
//

#include "79.h"
#include "gtest/gtest.h"

using namespace std;

TEST(WordSearch,t1){
    Solution s;
    vector<vector<char>> board(3);
    board[0]=vector<char>({'A','B','C','E'});
    board[1]=vector<char>({'S','F','C','S'});
    board[2]=vector<char>({'A','D','E','E'});
    EXPECT_EQ(true,s.exist(board,"ABCCED"));
}
TEST(WordSearch,t2){
    Solution s;
    vector<vector<char>> board(3);
    board[0]=vector<char>({'C','A','A'});
    board[1]=vector<char>({'A','A','A'});
    board[2]=vector<char>({'B','C','D'});
    EXPECT_EQ(true,s.exist(board,"AAB"));
}

int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
