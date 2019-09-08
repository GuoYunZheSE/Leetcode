# # Insert Delete GetRandom O(1)
# Details
# Runtime: 148 ms, faster than 34.36% of Python3 online submissions for Insert Delete GetRandom O(1).
# Memory Usage: 17.9 MB, less than 12.50% of Python3 online submissions for Insert Delete GetRandom O(1).
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.k=20
        self.hashtable={}
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        reminder=val%self.k
        if self.hashtable.__contains__(reminder):
            if val in self.hashtable[reminder]:
                return False
            else:
                temp=self.hashtable[reminder]
                temp.append(val)
                self.hashtable.update({reminder:temp})
                return True
        else:
            self.hashtable.setdefault(reminder,[val])
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        reminder=val%self.k
        if self.hashtable.__contains__(reminder):
            if val in self.hashtable[reminder]:
                temp = self.hashtable[reminder]
                temp.remove(val)
                if temp==[]:
                    self.hashtable.pop(reminder)
                else:
                    self.hashtable.update({reminder: temp})
                return True
            else:
                return False
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.hashtable)==0:
            return 0
        else:
            table=random.choice(list(self.hashtable.keys()))
            return random.choice(self.hashtable[table])


if __name__ == '__main__':
    obj = RandomizedSet()
    param_1 = obj.insert(2)
    q1 = obj.insert(2)
    param_1 = obj.insert(2)
    param_1 = obj.insert(2)
    param_1 = obj.insert(2)
    param_1 = obj.insert(2)
    param_1 = obj.insert(2)
    param_1 = obj.insert(2)
    param_2 = obj.remove(2)
    param_3 = obj.getRandom()