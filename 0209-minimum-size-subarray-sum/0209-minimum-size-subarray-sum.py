class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        c=len(nums)
        n=len(nums)
        sums=nums[0]

        while j<n:
            if sums>=target:
                c=min(c,j-i+1)
                if i<j:
                    sums-=nums[i]
                    i+=1
                else:
                    break
            else:
                if j<n-1:
                    j+=1
                    sums+=nums[j]
                else:
                    break
        if c == len(nums) and sum(nums)<target:
            return 0
            
        return c
        