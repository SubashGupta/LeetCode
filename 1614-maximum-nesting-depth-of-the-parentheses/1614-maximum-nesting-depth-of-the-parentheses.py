class Solution:
    def maxDepth(self, s: str) -> int:
        if s == "":
            return 0
        c=0
        maxi=0
        for i in s:
            if i == "(":
                c+=1
                maxi = max(c,maxi)
            elif i == ")":
                c-=1
        if c == 0:
            return maxi
        else:
            return 0
        