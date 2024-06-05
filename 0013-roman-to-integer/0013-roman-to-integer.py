class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M': 1000}  
        l = len(s)-1
        val = d[s[l]]
        for i in range(l-1, -1, -1):
            if d[s[i]]>=d[s[i+1]]:
                val+=d[s[i]]
            elif d[s[i]]<d[s[i+1]]:
                val-=d[s[i]]
        return val
            
        