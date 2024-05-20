class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        conditions = n/3
        op=[]
        nums.sort()
        c=1
        maxval = nums[0]
        maxvalcount = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                c+=1
            else:
                if c>conditions:
                    c = 1
                    op.append(nums[i-1])
                else:
                    c = 1
        if c>conditions:
            op.append(nums[-1])
        return op