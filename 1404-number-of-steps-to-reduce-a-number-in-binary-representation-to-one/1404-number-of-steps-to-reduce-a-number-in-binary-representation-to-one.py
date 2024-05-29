class Solution:
    def numSteps(self, s: str) -> int:
        binval = int(s,2)
        c=0
        while binval != 1:
            if binval%2==1:
                binval = (binval+1)
            else:
                binval//=2
            c+=1
        return c