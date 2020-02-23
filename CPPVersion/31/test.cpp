//
// Created by 郭蕴喆 on 2020/2/24.
//

#include "31.h"
#include "gtest/gtest.h"

using namespace std;

TEST(Next_Permutation,t1){
    Solution s;
    vector<int> nums({1,2,3});
    s.nextPermutation(nums);
    EXPECT_EQ(vector<int> ({1,3,2}),nums);
}
TEST(Next_Permutation,t2){
    Solution s;
    vector<int> nums({3,2,1});
    s.nextPermutation(nums);
    EXPECT_EQ(vector<int> ({1,2,3}),nums);
}
TEST(Next_Permutation,t3){
    Solution s;
    vector<int> nums({1,1,5});
    s.nextPermutation(nums);
    EXPECT_EQ(vector<int> ({1,5,1}),nums);
}
TEST(Next_Permutation,t4){
    Solution s;
    vector<int> nums({4,2,0,2,3,2,0});
    s.nextPermutation(nums);
    EXPECT_EQ(vector<int> ({4,2,0,3,0,2,2}),nums);
}
int main(int argc, char ** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
