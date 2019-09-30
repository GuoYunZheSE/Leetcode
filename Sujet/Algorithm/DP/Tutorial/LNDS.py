# topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/
# The Python Solution of Problem:Find the length of the longest non-decreasing sequence.

class LNDS:
    def run(self,nums:list):
        res=[1]*len(nums)
        for eachnum in range(0,len(nums)):
            beforenum=0
            while beforenum<eachnum:
                if nums[beforenum]<=nums[eachnum]:
                    res[eachnum] = max(res[eachnum], res[beforenum] + 1)
                beforenum+=1
        return max(res)

if __name__ == '__main__':
    sol=LNDS()
    print(sol.run([5, 3, 4, 8, 6, 7,8]))
