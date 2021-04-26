# @Date    : 13:33 04/26/2021
# @Author  : ClassicalPi
# @FileName: 208.py
# @Software: PyCharm
import collections
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie=collections.defaultdict(dict)
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current=self.trie
        for c in word:
            if c not in current:
                current[c]={}
            current=current[c]
        current['End']=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current=self.trie
        for c in word:
            if c not in current:
                return False
            current=current[c]
        return current.get("End",False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current=self.trie
        for c in prefix:
            if c not in current:
                return False
            current=current[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)