//
// Created by 郭蕴喆 on 2020/2/20.
//
#include <gtest/gtest.h>
#include "324.h"

using namespace std;

TEST(Wiggle_Sort_2,t1){
    vector<int> M({{1, 5, 1, 1, 6, 4}});
    Solution s;
    EXPECT_EQ(M,s.wiggleSort(M));
}
TEST(Wiggle_Sort_2,t2){
    vector<int> M({{1, 3, 2, 2, 3, 1,5}});
    Solution s;
    EXPECT_EQ(M,s.wiggleSort(M));
}
TEST(Wiggle_Sort_2,t3){
    vector<int> M({1,1,2,1,2,2,1});
    Solution s;
    EXPECT_EQ(M,s.wiggleSort(M));
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}
