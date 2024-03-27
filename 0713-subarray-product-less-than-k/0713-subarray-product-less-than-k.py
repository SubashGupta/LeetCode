class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        c=0
        prod = 1
        caches  = True
        if k <=1:
            return 0
        while j<len(nums):
            if caches:
                prod *= nums[j]
            if prod<k:
                c+=j-i+1
                j+=1
                #print(c,i,j)
                caches = True
            else:
                prod//=nums[i]
                i+=1
                caches = False
        return c
                
        