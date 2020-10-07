# @Date    : 12:30 10/06/2020
# @Author  : ClassicalPi
# @FileName: 36.py
# @Software: PyCharm

class Solution:

    def isValidSudoku(self, board: [[str]]) -> bool:
        columns={}

        for row_index,eachrow in enumerate(board):
            row=[]
            for col_index,val in enumerate(eachrow):
                #Check Row
                if val=='.':
                    val=0
                else:
                    if val in row:
                        return False
                    row.append(val)

                if columns.__contains__(col_index):
                    # Check Column
                    if val !=0 and val in columns[col_index]:
                        return False
                    else:
                        columns[col_index].append(val)
                else:
                    columns.setdefault(col_index,[val])

        # Check sub-box
        sub_box={}
        for i in range(9):
            col=i//3
            for j in range(9):
                row=j//3
                if sub_box.__contains__((col,row)):
                    if columns[i][j]!=0 and columns[i][j] in sub_box[(col,row)]:
                        return False
                    else:
                        sub_box[(col,row)].append(columns[i][j])
                else:
                    sub_box.setdefault((col,row),[columns[i][j]])
        return True

if __name__ == '__main__':
    S=Solution()
    print(S.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))