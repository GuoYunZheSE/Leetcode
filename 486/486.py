# Class:Medium
# Data:Friday, 26/01/2019
def PredictTheWinner(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return winner(nums,0,nums.__len__()-1,1)>=0

# Runtime: 8484 ms, faster than 5.14% of Python3 online submissions for Predict the Winner.
# Memory Usage: 13.3 MB, less than 6.82% of Python3 online submissions for Predict the Winner.
def winner(nums,s,e,turn):
    if s==e:
        return turn*nums[s]
    a=turn*nums[s]+winner(nums,s+1,e,-turn)
    b=turn*nums[e]+winner(nums,s,e-1,-turn)
    return turn*max(turn*a,turn*b)


if __name__ == '__main__':
    nums=[1,5,8,4]
    PredictTheWinner(nums)