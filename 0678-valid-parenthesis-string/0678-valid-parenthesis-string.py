class Solution:
    def checkValidString(self, s: str) -> bool:
        start=0
        end=0
        last=len(s)-1
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "*":
                start+=1
            else:
                start-=1
            if s[last-i] == ")" or s[last-i] == "*":
                end+=1
            else:
                end-=1
            if start<0 or end<0:
                return False
        return True