class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d={}
        for i in hand:
            d[i]=d.get(i,0)+1
        while len(d)>0:
            minval = min(d)
            for i in range(groupSize):
                if d.get(minval):
                    d[minval]-=1
                    if d[minval] == 0:
                        del d[minval]
                    minval+=1
                else:
                    return False
        return True
            