class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        c1=0
        oddcount=0
        for i in s:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if d[i]%2==0:
                c1+=d[i]
            else:
                c1+=d[i]-1
                oddcount=1
        return c1+oddcount