# Runtime: 40 ms, faster than 84.34% of Python3 online submissions for Largest Time for Given Digits.
# Memory Usage: 13.3 MB, less than 6.25% of Python3 online submissions for Largest Time for Given Digits.
class Solution:
    def largestTimeFromDigits(self, A: [int]) -> str:
        dis_hour="2"
        bit_hour="11"
        dis_min="11"
        bit_min="11"
        find_dis_hour=False
        find_bit_hour=False
        find_bit_min=False
        fin_dis_min=False
        A=sorted(A,reverse=True)
        for i in A:
            if i <= int(dis_hour):
                if i !=2:
                    dis_hour = str(i)
                    find_dis_hour = True
                    A.remove(int(dis_hour))
                    break
                else:
                    if A[1]>=6:
                        continue
                    else:
                        dis_hour = str(i)
                        find_dis_hour = True
                        A.remove(int(dis_hour))
                        break
        for a in A:
            if not find_dis_hour:return ""
            if (int(dis_hour)==2 and a<=3 and not find_bit_hour) or (int(dis_hour)<2 and a<=9 and not find_bit_hour):
                bit_hour=str(a)
                find_bit_hour=True
                continue
            if a<=5 and not fin_dis_min:
                dis_min=str(a)
                fin_dis_min=True
                continue
            if a<=9 and not find_bit_min:
                bit_min=str(a)
                find_bit_min=True
                continue
        if (int(dis_hour)<2):
            temp=bit_hour
            if bit_min>bit_hour:
                bit_hour=bit_min
                bit_min=temp
            if dis_min>bit_hour:
                bit_hour=dis_min
                dis_min=temp
                temp=bit_hour
        if  find_bit_min and fin_dis_min and find_bit_hour and find_dis_hour:
            return "{}{}:{}{}".format(dis_hour,bit_hour,dis_min,bit_min)
        else:
            return ""


if __name__ == '__main__':
    A=[1,2,3,4]
    S=Solution()
    A=S.largestTimeFromDigits(A)
    print(A)