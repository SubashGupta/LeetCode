class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        while i<=len(s)-2:
            if s[i]!=s[i+1]:
                if (ord(s[i])+32 == ord(s[i+1])) or (ord(s[i]) == ord(s[i+1])+32):
                    s=s[:i]+s[i+2:]
                    if i!=0:
                        i-=1
                else:
                    i+=1
            else:
                i+=1
        return s
            
            
                
        