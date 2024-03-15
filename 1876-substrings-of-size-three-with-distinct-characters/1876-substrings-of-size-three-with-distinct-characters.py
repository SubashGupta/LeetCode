class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)>=3:
            a=s[0]
            b=s[1]
            c=s[2]
            op=0
            for i in range(3,len(s)):
                if a!=b and b!=c and c!=a:
                    op+=1
                a,b,c = b,c,s[i]
            if a!=b and b!=c and c!=a:
                op+=1
            return op
        else:
            return 0
            
        
                    
                
            
        