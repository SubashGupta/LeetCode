class Solution:
    def minSwaps(self, s: str) -> int:
        opens=0
        close=0
        swapcount=0
        j=len(s)-1
        l = list(s)
        for i in range(len(s)):
            if l[i] == "[":
                opens+=1
            else:
                close+=1
            if close>opens:
                while j > i:
                    if l[j] == "[":
                        l[j],l[i]=l[i],l[j]
                        j-=2
                        swapcount+=1
                        close-=1
                        opens+=1
                        break
                    j-=1
        return swapcount