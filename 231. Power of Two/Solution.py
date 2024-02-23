class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        elif n==0:
            return False
        p=n
        while p!=0:
            if p==1:
                return True
            if p%2==0:
                p=p//2
            else:
                return False
        return True


        