def Eat(n:int):
    memory = {}
    def recur(cur:int):
        if cur <= 2:
            return cur

        res = 0
        if memory.get(cur-1,0)!=0:
            res += memory[cur-1]
        else:
            temp = recur(cur-1)
            memory[cur-1] = temp
            res += temp
        if memory.get(cur-2,0)!=0:
            res += memory[cur-2]
        else:
            temp = recur(cur-2)
            memory[cur-2]=temp
            res += temp
        return res

    return recur(n)
# 123425
if __name__ == '__main__':
    print(Eat(1000))