import typing
class Solution:
    def intersection(self, nums1: typing.List[int], nums2: typing.List[int]) -> typing.List[int]:
        res={}
        if len(nums1)>=len(nums2):
            smaller=nums1
            bigger=nums2
        else:
            smaller=nums2
            bigger=nums1

        for each in smaller:
            if bigger.__contains__(each):
                if not res.__contains__(each):
                    res.setdefault(each,1)
        return list(res.keys())