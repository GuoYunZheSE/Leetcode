//
// Created by 郭蕴喆 on 2020/2/24.
//

#include "1356.h"
#include "gtest/gtest.h"

using namespace std;

TEST(sortByBits,t1){
    Solution s;
    vector<int> nums({0,1,2,3,4,5,6,7,8});
    s.sortByBits(nums);
    EXPECT_EQ(vector<int> ({0,1,2,4,8,3,5,6,7}),nums);
}

TEST(sortByBits,t2){
    Solution s;
    vector<int> nums({1024,512,256,128,64,32,16,8,4,2,1});
    s.sortByBits(nums);
    EXPECT_EQ(vector<int> ({1,2,4,8,16,32,64,128,256,512,1024}),nums);
}

TEST(sortByBits,t3){
    Solution s;
    vector<int> nums({2,3,5,7,11,13,17,19});
    s.sortByBits(nums);
    EXPECT_EQ(vector<int> ({2,3,5,17,7,11,13,19}),nums);
}

TEST(sortByBits,t4){
    Solution s;
    vector<int> nums({10000,10000});
    s.sortByBits(nums);
    EXPECT_EQ(vector<int> ({10000,10000}),nums);
}
TEST(sortByBits,t5){
    Solution s;
    vector<int> nums({10,100,1000,10000});
    s.sortByBits(nums);
    EXPECT_EQ(vector<int> ({10,100,10000,1000}),nums);
}
TEST(sortByBits,t6){
    Solution s;
    vector<int> nums({1111,7644,1107,6978,8742,1,7403,7694,9193,4401,377,8641,5311,624,3554,6631});
    s.sortByBits(nums);
    EXPECT_EQ(vector<int> ({1,624,1107,4401,8641,8742,377,1111,6978,3554,7694,9193,5311,6631,7403,7644}),nums);
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}