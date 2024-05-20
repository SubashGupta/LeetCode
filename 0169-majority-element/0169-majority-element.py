class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        c=1
        maxcount=0
        maxval = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                c+=1
            else:
                if maxcount < c:
                    maxval = nums[i-1]
                    maxcount = c
                    c=1
                else:
                    c=1
        if maxcount<c:
            maxval = nums[-1]
        return maxval
                    