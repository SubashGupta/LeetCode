class Solution:
    def numSteps(self, s: str) -> int:
        '''
        binval = int(s,2)
        c=0
        while binval != 1:
            if binval%2==1:
                binval = (binval+1)
            else:
                binval//=2
            c+=1
        return c
        '''
        count=0
        carry=0
        l=len(s)-1
        while l>0:
            if int(s[l])+carry == 0:
                carry = 0
                count+=1
            elif int(s[l])+carry == 2:
                count+=1
                carry = 1
            else:
                count+=2
                carry=1
            l-=1
        if carry ==1:
            count+=1
        return count
                