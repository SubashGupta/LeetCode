class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        i=0
        n=len(code)
        op=[0]*n
        if k>0:
            sums=sum(code[1:k+1])
            op[0] = sums
            for j in range(1,len(code)):
                sums+=code[(k+j)%n]-code[j]
                op[j] = sums
        elif k<0:
            sums=sum(code[k:])
            print(sums)
            op[0] = sums
            for j in range(1,len(code)):
                print(code[(-k+j-1)%n], code[j-1])
                sums+=code[j-1]-code[(k+j-1)%n]
                op[j] = sums
        else:
            return op
        return op
        