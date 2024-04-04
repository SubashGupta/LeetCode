class Solution:
    def maxDepth(self, s: str) -> int:
        if s == "":
            return 0
        stacks = []
        c=0
        maxi=0
        for i in s:
            if i == "(":
                stacks.append(i)
                c+=1
                maxi = max(c,maxi)
            elif i == ")":
                stacks.pop()
                c-=1
        return maxi
        
        