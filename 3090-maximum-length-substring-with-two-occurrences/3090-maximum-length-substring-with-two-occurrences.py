class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i=0
        d={}
        j=0
        maxlength = float('-inf')
        while j<len(s):
            if s[j] not in d:
                d[s[j]]=0
            d[s[j]]+=1
            while d[s[j]]>2:
                d[s[i]]-=1
                if d[s[i]] == 0:
                    del d[s[i]]
                i+=1
            maxlength = max(maxlength, j-i+1)
            j+=1
        return maxlength
        