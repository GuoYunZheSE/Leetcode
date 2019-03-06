# Class:Hard
# Data:Wednesday, 06/03/2019
# Runtime: 3896 ms, faster than 15.98% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 16.3 MB, less than 39.42% of Python3 online submissions for Merge k Sorted Lists.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        elif len(lists)==1:
            return lists[0]
        else:
            temp=ListNode(-99999)
            first_left=temp
            first_right=temp
            for eachlist in range(0,len(lists)):
                first_left = temp
                first_right = temp
                second_left=lists[eachlist]
                second_right=lists[eachlist]
                while second_left:
                    if second_left.val < first_left.val:
                        while second_right.next and (second_right.next).val <= first_left.val:
                            second_right = second_right.next
                        second_left = second_right.next
                        second_right.next = first_left
                        second_right = second_left
                    if second_left.val >= first_left.val:
                        while first_left.next and (first_left.next).val <= second_left.val:
                            first_left = first_left.next
                        if first_left.next:
                            first_right = first_left.next
                            while second_right.next and (second_right.next).val <= first_right.val:
                                second_right = second_right.next
                            first_left.next = second_left
                            second_left = second_right.next
                            second_right.next = first_right
                            second_right = second_left
                        else:
                            first_left.next = second_left
                            second_left = None
                            second_right = None
        return temp.next
if __name__ == '__main__':
    L=[[-2,1,4,5],[-2,5,6],[-2,0]]
    S=[]
    for l in L:
         s=ListNode(l[0])
         nl=s
         for i in range(1,l.__len__()):
             nl.next=ListNode(l[i])
             nl=nl.next
         S.append(s)
    answer=Solution
    answer.mergeKLists(answer,S)