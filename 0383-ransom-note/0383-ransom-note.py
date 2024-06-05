class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in ransomNote:
            d[i]=d.get(i,0)+1
        
        for j in magazine:
            x=d.get(j,0)
            if x == 0:
                pass
            else:
                d[j]-=1
                if d[j] == 0:
                    del d[j]
        if len(d)==0:
            return True
        else:
            return False
        