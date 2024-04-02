class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        new=""
        if len(set(s)) == len(set(t)):
            for i in range(len(s)):
                if s[i] not in d:
                    d[s[i]] =t[i]
            for i in range(len(s)):
                new+=d[s[i]]
            return new == t
        else:
            return False
            
        