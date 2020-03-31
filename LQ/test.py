# @Date    : 12:27 03/28/2020
# @Author  : ClassicalPi
# @FileName: test.py
# @Software: PyCharm

def sublist(x: []):
    sublist2 = []
    count = 0
    if x == None:
        return None
    while count < len(x) and x[count] != 5:
        sublist2.append(x[count])
        count += 1
    return sublist2


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = ["wonderful","incredible"]
def strip_punctuation(x):
    for i in punctuation_chars:
        x = x.replace(i, " ")
    return x


def get_pos(x):
    x = x.lower()
    x = x.split(" ")
    ct = 0
    for i in x:
        if i in positive_words:
            ct += 1
    return ct
if __name__ == '__main__':
    x="""Testing "what a truly wonderful day it is today! #incredible"""
    x=strip_punctuation(x)
    print(x)
    print(get_pos(x))
