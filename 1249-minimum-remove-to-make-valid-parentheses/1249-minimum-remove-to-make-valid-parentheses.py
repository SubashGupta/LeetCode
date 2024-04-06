class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lst=[]
        left=0
        right=0
        for i in range(len(s)):
            if s[i] == "(":
                left+=1
            elif s[i] == ")":
                right+=1
            if right>left:
                right-=1
            else:
                lst.append(s[i])
        op=""
        while lst:
            x = lst.pop()
            if left>right and x == "(":
                left-=1
            else:
                op+=x
        return op[::-1]