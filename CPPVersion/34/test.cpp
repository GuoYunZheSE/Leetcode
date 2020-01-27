//
// Created by 郭蕴喆 on 2020/1/27.
//

#include <gtest/gtest.h>
#include "34.h"

using namespace std;
TEST(_34,t1){
    vector<int> nums({5,7,7,8,8,10});
    int target=8;
    Solution s;
    EXPECT_EQ(vector<int> ({3,4}),s.searchRange(nums,target));
}
TEST(_34,t2){
    vector<int> nums({5,7,7,8,8,10});
    int target=6;
    Solution s;
    EXPECT_EQ(vector<int> ({-1,-1}),s.searchRange(nums,target));
}
TEST(_34,t3){
    vector<int> nums({1});
    int target=1;
    Solution s;
    EXPECT_EQ(vector<int> ({0,0}),s.searchRange(nums,target));
}
TEST(_34,t4){
    vector<int> nums({});
    int target=1;
    Solution s;
    EXPECT_EQ(vector<int> ({-1,-1}),s.searchRange(nums,target));
}
int main(int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();  // 执行所有的 test case
}