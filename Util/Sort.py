import typing
def bubbleSort(compare:typing.Callable[[int,int],bool],nums:[])->[]:
    for i in range(0,len(nums)-1):
        count=0
        for j in range(0,len(nums)-1):
            bigger=compare(nums[j],nums[j+1])
            if bigger:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                count+=1
        if count==0:
            return nums
    return nums
# def quickSort(compare:typing.Callable[[int,int],bool],nums:[])->[]:
#