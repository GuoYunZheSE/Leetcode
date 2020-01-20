class Solution:
    def diffWaysToCompute(self, input: str) -> [int]:

        self.memo = {}
        self.ops = ["+", "-", "*"]
        return self.dp(input)

    def dp(self, input):

        if input in self.memo:
            return self.memo[input]

        flag = False
        res = []
        for i, s in enumerate(input):
            if s in self.ops:
                flag = True
                left_res = self.dp(input[:i])
                right_res = self.dp(input[i + 1:])
                res += self.op(s, left_res, right_res)

        if not flag:
            res.append(int(input))

        return res

    @staticmethod
    def op(code, a_arr, b_arr):

        if code == "+":
            return [a + b for a in a_arr for b in b_arr]
        if code == "-":
            return [a - b for a in a_arr for b in b_arr]
        if code == "*":
            return [a * b for a in a_arr for b in b_arr]
if __name__ == '__main__':
    S="2*3-4*5"
    s=Solution()
    s.diffWaysToCompute(S)