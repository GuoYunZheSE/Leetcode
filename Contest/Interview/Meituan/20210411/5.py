# @Date    : 11:41 04/11/2021
# @Author  : ClassicalPi
# @FileName: 5.py
# @Software: PyCharm
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return l
class Solution:
    def order(self,P:[],V:[],Q:dict,K:int):
        layers=(sum(P)+Q[binarySearch(list(Q.keys()),0,len(list(Q.keys()))-1,sum(P))])//min(P)
        dp=[[0 for i in P] for j in layers]
