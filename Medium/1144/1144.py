class Solution:
    def __init__(self):
        self.evenGreaterMoves=0
        self.oddGreaterMoves=0
    def makeEvenGreater(self,orign_nums:[int],index:int,even_nums:[int]):
        indexDecrease=0
        if index==0:
            diff=orign_nums[0]-orign_nums[1]
            indexDecrease=1
        else:
            if index==len(orign_nums)-1:
               diff=orign_nums[-1]-orign_nums[-2]
               indexDecrease=-2
            else:
                if orign_nums[index]<=orign_nums[index-1]:
                    diff = orign_nums[index] - orign_nums[index-1]
                    self.evenGreaterMoves += abs(diff) + 1
                    even_nums[index-1] = orign_nums[index-1] - abs(diff) - 1
                if orign_nums[index]<=orign_nums[index+1]:
                    diff = orign_nums[index] - orign_nums[index+1]
                    self.evenGreaterMoves += abs(diff) + 1
                    even_nums[index+1] = orign_nums[index+1] - abs(diff) - 1
                diff=1
        if diff <= 0:
            self.evenGreaterMoves += abs(diff)+1
            even_nums[indexDecrease] = orign_nums[indexDecrease]-abs(diff)-1


    def makeOddGreater(self,orign_nums:[int],index:int,odd_nums:[int]):
        indexDecrease=0
        if index==len(orign_nums)-1:
            diff=orign_nums[-1]-orign_nums[-2]
            indexDecrease=-2
        else:
            if orign_nums[index] <= orign_nums[index - 1]:
                diff = orign_nums[index] - orign_nums[index - 1]
                self.oddGreaterMoves += abs(diff) + 1
                odd_nums[index - 1] = orign_nums[index - 1] - abs(diff) - 1
            if orign_nums[index] <= orign_nums[index + 1]:
                diff = orign_nums[index] - orign_nums[index + 1]
                self.oddGreaterMoves += abs(diff) + 1
                odd_nums[index + 1] = orign_nums[index + 1] - abs(diff) - 1
            diff = 1
        if diff <= 0:
            self.oddGreaterMoves+=abs(diff)+1
            odd_nums[indexDecrease]=orign_nums[indexDecrease]-abs(diff)-1

    def movesToMakeZigzag(self, nums: [int]) -> int:
        even_nums=nums.copy()
        odd_nums=nums.copy()
        for i in range(0,len(nums)):
            if i%2==0:
                self.makeEvenGreater(even_nums,i,even_nums)
            else:
                self.makeOddGreater(odd_nums,i,odd_nums)
        return min(self.oddGreaterMoves,self.evenGreaterMoves)

    def sprint(self,nums:[int]):
        even_nums=nums.copy()
        odd_nums=nums.copy()
        for i in range(0,len(nums)):
            if i%2==0:
                self.makeEvenGreater(even_nums,i,even_nums)
            else:
                self.makeOddGreater(odd_nums,i,odd_nums)
        print("even_nums:{} ".format(self.evenGreaterMoves),even_nums)
        print("odd_nums:{} ".format(self.oddGreaterMoves),odd_nums)

if __name__ == '__main__':
    S=Solution()
    A=[9,6,1,6,2]
    S.sprint(A)