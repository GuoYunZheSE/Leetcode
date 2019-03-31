# Date:31/03/2019
# Level:Easy
# Runtime: 124 ms, faster than 75.41% of Python3 online submissions for Design HashSet.
# Memory Usage: 17.1 MB, less than 41.46% of Python3 online submissions for Design HashSet.
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict={}
    def add(self, key: int) -> None:
        hash=key%1000
        if self.dict.get(hash)==None:
            self.dict.update({hash:[key]})
        else:
            old=self.dict.get(hash)
            if key not in old:
                old.append(key)
                self.dict.update({hash: old})
    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        else:
            hash=key%1000
            old=self.dict.get(hash)
            old.remove(key)
            if old.__len__()==0:
                self.dict.update({hash:None})
            else:
                self.dict.update({hash:old})
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash=key%1000
        if self.dict.get(hash)==None:
            return False
        else:
            if key in self.dict.get(hash):
                return True
            else:
                return False

if __name__ == '__main__':
    A=MyHashSet()
    A.add(1)
    A.add(2)
    A.add(2)
