import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return sum(nums)
        else:
            s=0
            maxi = max(nums)
            for i in range(len(nums)):
                s+=nums[i]
                if s>0:
                    maxi = max(s,maxi)
                if s<0:
                    s=0
            return maxi
                    
                    
            
        