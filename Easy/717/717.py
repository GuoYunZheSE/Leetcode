# Success
# Details
# Runtime: 60 ms, faster than 73.44% of Python3 online submissions for 1-bit and 2-bit Characters.
# Memory Usage: 13.5 MB, less than 20.00% of Python3 online submissions for 1-bit and 2-bit Characters.
class Solution:
    def isOneBitCharacter(self, bits: [int]) -> bool:
        if len(bits)<=1:
            return True
        n=len(bits)
        i=0
        while i<n-1:
            if bits[i]==0:
                if i==n-2:
                    return True
                i+=1
            if bits[i]==1:
                if i==n-2:
                    return False
                if i==n-3:
                    return True
                if i==n-1:
                    return False
                i+=2
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # if len(bits) < 2: return True
        # # for i in range(len(bits)):
        # i=0
        # while i < len(bits):
        #     if bits[i] == 1:
        #         i = i+2
        #         ans = False
        #     else:
        #         i = i+1
        #         ans = True
        # return ans
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0