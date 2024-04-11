class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stacks=[]
        for i in range(len(num)):
            while stacks and k>0 and stacks[-1]>num[i]:
                stacks.pop()
                k-=1
            stacks.append(num[i])
        stacks = stacks[:-k] if k > 0 else stacks
        x = ''.join(stacks).lstrip("0")
        if x:
            return x
        else:
            return "0"