# Runtime: 956 ms, faster than 8.57% of Python3 online submissions for Sliding Window Median.
# Runtime: 576 ms, faster than 12.00% of Python3 online submissions for Sliding Window Median.(Use Bisec)
# Memory Usage: 15.6 MB, less than 20.00% of Python3 online submissions for Sliding Window Median.
import bisect
class Solution:
    def medianSlidingWindow(self, nums: [int], k: int) -> [float]:
        if len(nums)==0:
            return None
        else:
            window=nums[0:k]
            sortedArray=nums[0:k]
            sortedArray.sort()
            result=[self.findMedianFromSortedArray(sortedArray)]
            for i in range(k,len(nums)):
                window,sortedArray=self.moveWindow(window,sortedArray,nums[i])
                result.append(self.findMedianFromSortedArray(sortedArray))
            return result

    def moveWindow(self,window:list,sortedArray:list,next:int)->[list,list]:
        left=window[0]
        window.append(next)
        window=window[1:]
        sortedArray.remove(left)
        bisect.insort(sortedArray, next)
        return window,sortedArray
    def findMedianFromSortedArray(self,sortedArray:list)->float or None:
        length=len(sortedArray)
        if length==0:
            return None
        else:
            if length%2==0:
                index=int(length/2)
                return (sortedArray[index]+sortedArray[index-1])/2
            else:
                index=int(length/2)
                return sortedArray[index]
if __name__ == '__main__':
    n=[1, 3, -1, -3, 5, 3, 6, 7]
    k=3
    S=Solution()
    print(S.medianSlidingWindow(n,k))