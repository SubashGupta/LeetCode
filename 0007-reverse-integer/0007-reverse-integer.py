class Solution:
    def reverse(self, x: int) -> int:
        s=0
        flag=False
        if x<0:
            flag = True
            x = x*(-1)
        while x!=0:
            rem = x%10
            s=s*10+rem
            x=x//10
        
        if s > (2**31) - 1:
            return 0
        else:
            if flag:
                return -s
            else:
                return s