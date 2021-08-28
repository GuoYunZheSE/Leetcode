# s = ""
# t = ""
# 在字符串s里找出包含t所有子母的最小子串
# s = "ebanc"
# t = "abc"
# return "banc"
# 假设最小子串只有一个，没有的话返回""

import collections

def check(window:{},keys:[]):
    for key in keys:
        if window.get(key,0)<1:
            return False
    return True
def MinSubString(s:str,t:str)->str:
    if t == "" or s == "":
        return ""
    window = {}
    window_deque = collections.deque([])
    t_dic = collections.Counter(t)
    res = {}
    for letter in s:
        if letter in window:
            window[letter] += 1
        else:
            window[letter] = 1
        window_deque.append(letter)
        Found = False
        temp = ""
        while check(window,list(t_dic.keys())):
            temp = window_deque.popleft()
            window[temp] -= 1
            Found = True
        if Found:
            res.setdefault(len(window_deque)+1,temp+"".join(window_deque))
    return res[min(list(res.keys()))]

if __name__ == '__main__':
    print(MinSubString("ebanc", "abc"))