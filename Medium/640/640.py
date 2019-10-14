# # Input: "x+5-3+x=6+x-2"
# # Output: "x=2"
# class Solution:
#     def solveEquation(self, equation: str) -> str:
#         equation_left, equation_right = equation.split('=')
#
#         left_constant = 0
#         left_variable = 0
#
#         right_constant = 0
#         right_variable = 0
#
#         op=1
#         i=0
#         while i < len(equation_left):
#             if equation_left[i].isdecimal():
#                 dec=''
#                 for j in range(i,len(equation_left)):
#                     if equation_left[j].isdecimal():
#                         dec+=equation_left[j]
#                         if j==len(equation_left)-1:
#                             left_constant += int(dec)*op
#                             break
#                     elif equation_left[j] == 'x':
#                         left_variable += int(dec)*op
#                         i=j
#                         break
#                     else:
#                         left_constant+=int(dec)*op
#                         i=j-1
#                         break
#             else:
#                 if equation_left[i] == '-':
#                     op = -1
#                 elif equation_left[i] == '+':
#                     op = 1
#                 elif equation_left[i] == 'x':
#                     left_variable += 1 * op
#             i += 1
#
#         op=1
#         i=0
#         while i < len(equation_right):
#             if equation_right[i].isdecimal():
#                 dec=''
#                 for j in range(i,len(equation_right)):
#                     if equation_right[j].isdecimal():
#                         dec+=equation_right[j]
#                         if j==len(equation_right)-1:
#                             right_constant += int(dec)*op
#                             i+=1
#                             break
#                     elif equation_right[j] == 'x':
#                         right_variable += int(dec)*op
#                         i=j
#                         break
#                     else:
#                         right_constant+=int(dec)*op
#                         i=j-1
#                         break
#             else:
#                 if equation_right[i] == '-':
#                     op=-1
#                 elif equation_right[i]=='+':
#                     op=1
#                 elif equation_right[i] == 'x':
#                     right_variable += 1*op
#             i += 1
#
#         variable=left_variable-right_variable
#         constant=right_constant-left_constant
#
#         if variable==0:
#             if constant==0:
#                 return "Infinite solutions"
#             else:
#                 return "No solution"
#         else:
#             return "x={}".format(int(constant/variable))
class Solution:
    def solveEquation(self, E: str) -> str:
    	[a,b] = (lambda x: [x.real,x.imag])(eval(E.replace('x','j').replace('=','-(')+')', {'j': 1j}))
    	return 'x=' + str(int(-a//b)) if b else 'Infinite solutions' if not a else 'No solution'
if __name__ == '__main__':
    S=Solution()
    print(S.solveEquation("1-x+x-x+x+x=99"))