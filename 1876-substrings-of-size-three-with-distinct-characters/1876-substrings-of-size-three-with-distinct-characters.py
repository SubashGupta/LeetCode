class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k=3
        lst=[]
        for i in range(len(s)-k+1):
            if len(set(s[i:k+i])) == k:
                lst.append(s[i:k+i])
        return len(lst)
            
        
                    
                
            
        