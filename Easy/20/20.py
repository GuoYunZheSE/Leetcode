class Solution:
    def __init__(self):
        self.stack_open=[]
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        else:
            for each in s:
                if each=='(':
                    self.stack_open.append('(')
                    continue
                if each=='{':
                    self.stack_open.append('{')
                    continue
                if each=='[':
                    self.stack_open.append('[')
                    continue
                if each==')':
                    if len(self.stack_open)<=0 or self.stack_open.pop()!='(':
                        return False
                    continue
                if each=='}':
                    if len(self.stack_open)<=0 or self.stack_open.pop()!='{':
                        return False
                    continue
                if each==']':
                    if len(self.stack_open)<=0 or self.stack_open.pop()!='[':
                        return False
                    continue
            if len(self.stack_open)==0:
                return True
            else:
                return False
if __name__ == '__main__':
    S=Solution()
    print(S.isValid("{[]}"))