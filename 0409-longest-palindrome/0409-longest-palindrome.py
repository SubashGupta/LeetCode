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
                c1+=d[i]-1 #Because if there are 3 ccc's then we take 2 of them sure.
                oddcount=1 #stating that one odd char is considered for middle
        return c1+oddcount