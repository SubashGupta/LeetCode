class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s1=n*(n+1)//2
        s2=(n*(n+1)*(2*(n)+1))//6
        s=0
        sn=0
        for i in nums:
            s+=i
            sn+=i*i
        val1=s1-s
        val2=s2-sn
        val2=val2//val1
        
        missed = (val1+val2)//2
        repeated = val2-missed
        return repeated,missed
            