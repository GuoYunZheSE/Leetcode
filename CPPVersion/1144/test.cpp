//
// Created by 郭蕴喆 on 2020/1/19.
//

//
// Created by 郭蕴喆 on 2020/1/19.
//

#include "1144.h"
#include <gtest/gtest.h>
using namespace std;

TEST(Zigzag,t1){
    vector<int> nums({2,7,10,9,8,9});;
    Solution sol;
    int res=sol.movesToMakeZigzag(nums);
    EXPECT_EQ(4,res);
}
TEST(Zigzag,t2){
    vector<int> nums({9,6,1,6,2});
    Solution sol;
    int res=sol.movesToMakeZigzag(nums);
    EXPECT_EQ(4,res);
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}