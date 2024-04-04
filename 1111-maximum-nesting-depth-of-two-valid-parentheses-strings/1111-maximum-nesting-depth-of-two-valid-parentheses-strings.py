class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        k={}
        op=[]
        for i in seq:
            k[i]=k.get(i,0)+1
            if k.get(i,0)%2 == 0:
                op.append(1)
            else:
                op.append(0)
        return op
        